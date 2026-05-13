from __future__ import annotations

import argparse
import itertools
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd


LANG_MARKER_RE = re.compile(
    r"(?im)^\s*(?:python|java|javascript|c\+\+|cpp|ruby|go)\s*$"
)
SNIPPET_SEP_RE = re.compile(
    r"\n(?:\s*\n){2,}(?=\s*(?:def|class|from|import|@)\b)"
)
FALLBACK_SEP_RE = re.compile(r"\n\s*\n\s*\n+")


@dataclass(frozen=True)
class FileRecord:
    filename: str
    path: Path
    source_group: str
    clone_type: str
    problem_id: int | None


def load_labels(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, header=None, names=["filename", "label"])
    if df["filename"].duplicated().any():
        dup_count = int(df["filename"].duplicated().sum())
        raise ValueError(f"Duplicate filenames in labels CSV: {dup_count}")
    if not set(df["label"].unique()).issubset({0, 1}):
        raise ValueError("Labels must be binary (0/1).")
    return df


def parse_problem_id(filename: str) -> int | None:
    patterns = [
        r"^Clone_(\d+)\.py$",
        r"^4_Clone_(\d+)\.py$",
        r"^Gpt_false_pair_(\d+)\.py$",
    ]
    for pattern in patterns:
        match = re.match(pattern, filename)
        if match:
            return int(match.group(1))
    return None


def classify_file(path: Path) -> tuple[str, str]:
    path_str = str(path).replace("\\", "/")
    if "/true_semantic_clones/py/MT3/" in path_str:
        return "true_semantic_mt3", "type_III"
    if "/true_semantic_clones/py/T4/" in path_str:
        return "true_semantic_t4", "type_IV"
    if "/false_semantic_clones/py/" in path_str:
        return "false_semantic", "non_clone"
    return "unknown", "unknown"


def discover_python_files(dataset_root: Path) -> dict[str, FileRecord]:
    files = list(dataset_root.glob("true_semantic_clones/py/MT3/*.py"))
    files += list(dataset_root.glob("true_semantic_clones/py/T4/*.py"))
    files += list(dataset_root.glob("false_semantic_clones/py/*.py"))

    mapping: dict[str, FileRecord] = {}
    for path in files:
        source_group, clone_type = classify_file(path)
        mapping[path.name] = FileRecord(
            filename=path.name,
            path=path,
            source_group=source_group,
            clone_type=clone_type,
            problem_id=parse_problem_id(path.name),
        )
    return mapping


def split_snippets(file_text: str) -> list[str]:
    text = file_text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return []

    blocks = [b.strip() for b in LANG_MARKER_RE.split(text) if b.strip()]
    snippets: list[str] = []

    for block in blocks:
        parts = [p.strip() for p in SNIPPET_SEP_RE.split(block) if p.strip()]
        snippets.extend(parts if len(parts) > 1 else [block])

    if len(snippets) < 2:
        fallback_parts = [p.strip() for p in FALLBACK_SEP_RE.split(text) if p.strip()]
        if len(fallback_parts) > len(snippets):
            snippets = fallback_parts

    return snippets


def iter_pair_rows(
    file_record: FileRecord,
    snippets: list[str],
    label: int,
    include_code: bool,
    dataset_root: Path,
) -> Iterable[dict]:
    for left_idx, right_idx in itertools.combinations(range(len(snippets)), 2):
        row = {
            "is_clone": int(label),
            "clone_type": file_record.clone_type if label == 1 else "non_clone",
            "source_group": file_record.source_group,
            "filename": file_record.filename,
            "file_path": str(file_record.path.relative_to(dataset_root)),
            "problem_id": file_record.problem_id,
            "snippet_index_a": left_idx,
            "snippet_index_b": right_idx,
        }
        if include_code:
            row["code_a"] = snippets[left_idx]
            row["code_b"] = snippets[right_idx]
        yield row


def build_pair_dataset(
    dataset_root: Path,
    labels_filename: str = "plagiarism_labels.csv",
    include_code: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    labels_path = dataset_root / labels_filename
    labels_df = load_labels(labels_path)
    file_map = discover_python_files(dataset_root)

    missing_files = sorted(set(labels_df["filename"]) - set(file_map))
    if missing_files:
        raise FileNotFoundError(
            f"{len(missing_files)} files listed in labels CSV were not found. "
            f"Examples: {missing_files[:5]}"
        )

    rows: list[dict] = []
    issues: list[dict] = []

    for item in labels_df.itertuples(index=False):
        file_record = file_map[item.filename]
        text = file_record.path.read_text(encoding="utf-8", errors="replace")
        snippets = split_snippets(text)

        if len(snippets) < 2:
            issues.append(
                {
                    "filename": file_record.filename,
                    "reason": "fewer_than_2_snippets",
                    "snippet_count": len(snippets),
                    "source_group": file_record.source_group,
                    "label": int(item.label),
                }
            )
            continue

        if file_record.source_group.startswith("true_semantic") and int(item.label) != 1:
            issues.append(
                {
                    "filename": file_record.filename,
                    "reason": "label_source_mismatch_true_expected_1",
                    "snippet_count": len(snippets),
                    "source_group": file_record.source_group,
                    "label": int(item.label),
                }
            )
        if file_record.source_group == "false_semantic" and int(item.label) != 0:
            issues.append(
                {
                    "filename": file_record.filename,
                    "reason": "label_source_mismatch_false_expected_0",
                    "snippet_count": len(snippets),
                    "source_group": file_record.source_group,
                    "label": int(item.label),
                }
            )

        rows.extend(
            iter_pair_rows(
                file_record=file_record,
                snippets=snippets,
                label=int(item.label),
                include_code=include_code,
                dataset_root=dataset_root,
            )
        )

    dataset_df = pd.DataFrame(rows)
    issues_df = pd.DataFrame(issues)
    return dataset_df, issues_df


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build pairwise clone detection dataset from folder-structured corpus."
    )
    parser.add_argument(
        "--dataset-root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Path containing plagiarism_labels.csv and clone folders.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "clone_pairs_dataset.csv",
        help="Output CSV path for the final pair dataset.",
    )
    parser.add_argument(
        "--issues-output",
        type=Path,
        default=Path(__file__).resolve().parent / "clone_pairs_issues.csv",
        help="Output CSV path for segmentation/consistency issues.",
    )
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="If set, do not include code_a/code_b columns; keep only references and labels.",
    )
    args = parser.parse_args()

    dataset_df, issues_df = build_pair_dataset(
        dataset_root=args.dataset_root,
        include_code=not args.metadata_only,
    )
    dataset_df.to_csv(args.output, index=False, encoding="utf-8")
    issues_df.to_csv(args.issues_output, index=False, encoding="utf-8")

    print(f"Dataset rows: {len(dataset_df)}")
    if not dataset_df.empty:
        print("Label distribution:")
        print(dataset_df["is_clone"].value_counts().sort_index().to_string())
        print("Clone type distribution:")
        print(dataset_df["clone_type"].value_counts().to_string())
    print(f"Issues rows: {len(issues_df)}")
    print(f"Dataset saved to: {args.output}")
    print(f"Issues saved to: {args.issues_output}")


if __name__ == "__main__":
    main()
