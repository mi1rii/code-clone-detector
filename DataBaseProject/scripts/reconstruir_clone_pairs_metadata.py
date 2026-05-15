#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path


TYPE_MAP = {
    "T1": ("type_I", "pares_t1"),
    "T2": ("type_II", "pares_t2"),
    "T3": ("type_III", "pares_t3"),
    "T4": ("type_IV", "pares_t4"),
}


def separar_snippets_basico(texto: str) -> list[str]:
    # Mantener criterio simple y robusto para validar 2 snippets por archivo.
    texto = texto.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not texto:
        return []
    partes = [p.strip() for p in re.split(r"\n\s*\n\s*\n+", texto) if p.strip()]
    if len(partes) >= 2:
        return partes
    return [texto]


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    tipos_base = base / "pares_clones" / "py" / "tipos_de_clones"
    out_csv = base / "clone_pairs_dataset_metadata.csv"

    rows: list[dict[str, str]] = []
    skipped = 0

    for t_folder, (clone_type, source_group) in TYPE_MAP.items():
        folder = tipos_base / t_folder
        if not folder.exists():
            raise FileNotFoundError(f"No existe carpeta: {folder}")
        for f in sorted(folder.glob("*.py")):
            contenido = f.read_text(encoding="utf-8", errors="replace")
            snippets = separar_snippets_basico(contenido)
            if len(snippets) < 2:
                skipped += 1
                continue

            m = re.search(r"_(\d+)\.py$", f.name)
            if not m:
                skipped += 1
                continue
            problem_id = int(m.group(1))
            rel = f.relative_to(base)

            rows.append(
                {
                    "is_clone": "1",
                    "clone_type": clone_type,
                    "source_group": source_group,
                    "filename": f.name,
                    "file_path": str(rel).replace("/", "\\"),
                    "problem_id": str(problem_id),
                    "snippet_index_a": "0",
                    "snippet_index_b": "1",
                }
            )

    fieldnames = [
        "is_clone",
        "clone_type",
        "source_group",
        "filename",
        "file_path",
        "problem_id",
        "snippet_index_a",
        "snippet_index_b",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as fw:
        writer = csv.DictWriter(fw, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # resumen
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["clone_type"]] = counts.get(r["clone_type"], 0) + 1

    print(f"[ok] metadata reconstruido: {out_csv}")
    print(f"[info] filas: {len(rows)}")
    print(f"[info] skipped: {skipped}")
    for k in sorted(counts.keys()):
        print(f"[info] {k}: {counts[k]}")


if __name__ == "__main__":
    main()

