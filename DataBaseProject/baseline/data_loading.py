from __future__ import annotations

#concentramos carga validacion limpieza y split por grupos para evitar leakage
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit


#declaramos las columnas que esperamos en el metadata
REQUIRED_METADATA_COLUMNS = [
    "is_clone",
    "clone_type",
    "source_group",
    "filename",
    "file_path",
    "problem_id",
    "snippet_index_a",
    "snippet_index_b",
]


@dataclass
class SplitResult:
    #guardamos los indices de train val y test ya separados por grupos
    train_idx: pd.Index
    val_idx: pd.Index
    test_idx: pd.Index


def load_metadata_csv(path: Path) -> pd.DataFrame:
    #cargamos el csv metadata y fallamos temprano si no existe
    if not path.exists():
        raise FileNotFoundError(f"Metadata CSV not found: {path}")
    return pd.read_csv(path)


def validate_metadata_schema(metadata_df: pd.DataFrame) -> tuple[bool, list[str]]:
    #revisamos que el metadata tenga columnas y valores basicos correctos
    errors: list[str] = []

    missing_cols = [col for col in REQUIRED_METADATA_COLUMNS if col not in metadata_df.columns]
    if missing_cols:
        errors.append(f"Missing required columns: {missing_cols}")

    if "filename" in metadata_df.columns and metadata_df["filename"].isna().any():
        errors.append("Column `filename` has null values.")
    if "file_path" in metadata_df.columns and metadata_df["file_path"].isna().any():
        errors.append("Column `file_path` has null values.")
    if "problem_id" in metadata_df.columns and metadata_df["problem_id"].isna().any():
        errors.append("Column `problem_id` has null values.")
    if "is_clone" in metadata_df.columns:
        allowed = {0, 1}
        found = set(pd.to_numeric(metadata_df["is_clone"], errors="coerce").dropna().unique())
        if not found.issubset(allowed):
            errors.append(f"Column `is_clone` has invalid values: {sorted(found - allowed)}")

    return len(errors) == 0, errors


def clean_metadata_rows(metadata_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    #convertimos tipos y apartamos filas con valores faltantes o invalidos
    cleaned = metadata_df.copy()

    cleaned["is_clone"] = pd.to_numeric(cleaned["is_clone"], errors="coerce")
    cleaned["problem_id"] = pd.to_numeric(cleaned["problem_id"], errors="coerce")
    cleaned["snippet_index_a"] = pd.to_numeric(cleaned["snippet_index_a"], errors="coerce")
    cleaned["snippet_index_b"] = pd.to_numeric(cleaned["snippet_index_b"], errors="coerce")

    invalid_mask = (
        cleaned["is_clone"].isna()
        | cleaned["problem_id"].isna()
        | cleaned["snippet_index_a"].isna()
        | cleaned["snippet_index_b"].isna()
        | cleaned["file_path"].isna()
        | cleaned["filename"].isna()
    )

    invalid_rows = cleaned.loc[invalid_mask].copy()
    if not invalid_rows.empty:
        invalid_rows["drop_reason"] = "invalid_or_missing_metadata_values"

    #nos quedamos solo con filas utilizables y fijamos tipos enteros
    cleaned = cleaned.loc[~invalid_mask].copy()
    cleaned["is_clone"] = cleaned["is_clone"].astype(int)
    cleaned["problem_id"] = cleaned["problem_id"].astype(int)
    cleaned["snippet_index_a"] = cleaned["snippet_index_a"].astype(int)
    cleaned["snippet_index_b"] = cleaned["snippet_index_b"].astype(int)

    return cleaned, invalid_rows


def _distribution_distance(
    full_df: pd.DataFrame,
    splits: dict[str, pd.DataFrame],
    target_col: str,
) -> float:
    #medimos que tan parecida queda la distribucion de clases entre splits y dataset completo
    overall = full_df[target_col].value_counts(normalize=True)
    classes = overall.index.tolist()
    distance = 0.0
    for split_df in splits.values():
        split_dist = split_df[target_col].value_counts(normalize=True)
        split_dist = split_dist.reindex(classes, fill_value=0.0)
        distance += float((split_dist - overall.reindex(classes, fill_value=0.0)).abs().sum())
    return distance


def grouped_train_val_test_split(
    df: pd.DataFrame,
    group_col: str,
    target_col: str,
    seed: int = 42,
    train_size: float = 0.7,
    val_size: float = 0.15,
    test_size: float = 0.15,
    max_attempts: int = 100,
) -> SplitResult:
    #hacemos split por grupos para que un mismo problem_id no caiga en train y test
    if round(train_size + val_size + test_size, 8) != 1.0:
        raise ValueError("train_size + val_size + test_size must sum to 1.0")

    best: tuple[float, SplitResult] | None = None
    required_classes = set(df[target_col].unique())
    temp_ratio = val_size + test_size
    rel_test_size = test_size / temp_ratio

    #intentamos varias semillas para mantener clases presentes y mejor equilibrio
    for attempt in range(max_attempts):
        random_seed = seed + attempt
        gss_train = GroupShuffleSplit(n_splits=1, train_size=train_size, random_state=random_seed)
        train_idx_arr, temp_idx_arr = next(
            gss_train.split(df, y=df[target_col], groups=df[group_col])
        )

        temp_df = df.iloc[temp_idx_arr]
        gss_temp = GroupShuffleSplit(
            n_splits=1, test_size=rel_test_size, random_state=random_seed
        )
        val_rel_idx, test_rel_idx = next(
            gss_temp.split(temp_df, y=temp_df[target_col], groups=temp_df[group_col])
        )

        train_idx = df.index[train_idx_arr]
        val_idx = temp_df.index[val_rel_idx]
        test_idx = temp_df.index[test_rel_idx]

        train_df = df.loc[train_idx]
        val_df = df.loc[val_idx]
        test_df = df.loc[test_idx]

        #pedimos que todas las clases existan en cada split cuando sea posible
        if required_classes.issubset(set(train_df[target_col].unique())) and required_classes.issubset(
            set(val_df[target_col].unique())
        ) and required_classes.issubset(set(test_df[target_col].unique())):
            distance = _distribution_distance(
                full_df=df,
                splits={"train": train_df, "val": val_df, "test": test_df},
                target_col=target_col,
            )
            result = SplitResult(train_idx=train_idx, val_idx=val_idx, test_idx=test_idx)
            if best is None or distance < best[0]:
                best = (distance, result)

    if best is None:
        #dejamos un respaldo si no encontramos una particion perfecta en los intentos
        gss_train = GroupShuffleSplit(n_splits=1, train_size=train_size, random_state=seed)
        train_idx_arr, temp_idx_arr = next(
            gss_train.split(df, y=df[target_col], groups=df[group_col])
        )
        temp_df = df.iloc[temp_idx_arr]
        gss_temp = GroupShuffleSplit(n_splits=1, test_size=rel_test_size, random_state=seed)
        val_rel_idx, test_rel_idx = next(
            gss_temp.split(temp_df, y=temp_df[target_col], groups=temp_df[group_col])
        )
        return SplitResult(
            train_idx=df.index[train_idx_arr],
            val_idx=temp_df.index[val_rel_idx],
            test_idx=temp_df.index[test_rel_idx],
        )

    return best[1]


def split_statistics(
    df: pd.DataFrame,
    split_col: str,
    target_col: str,
    group_col: str,
) -> list[dict[str, Any]]:
    #resumimos filas grupos y distribucion de clases por split para auditar el corte
    stats: list[dict[str, Any]] = []
    for split_name, split_df in df.groupby(split_col):
        counts = split_df[target_col].value_counts().to_dict()
        stats.append(
            {
                "split": split_name,
                "rows": int(len(split_df)),
                "unique_groups": int(split_df[group_col].nunique()),
                "class_distribution": {str(k): int(v) for k, v in counts.items()},
            }
        )
    return stats


def balance_training_dataframe(
    train_df: pd.DataFrame,
    target_col: str,
    strategy: str = "undersample",
    seed: int = 42,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    #balanceamos solo el split de entrenamiento para reducir sesgo por clases mayoritarias
    if strategy not in {"none", "undersample", "oversample"}:
        raise ValueError("strategy must be one of: none, undersample, oversample")

    original_counts = train_df[target_col].value_counts()
    info: dict[str, Any] = {
        "strategy": strategy,
        "target_col": target_col,
        "rows_before": int(len(train_df)),
        "class_distribution_before": {str(k): int(v) for k, v in original_counts.items()},
    }

    if strategy == "none" or len(original_counts) <= 1:
        info["rows_after"] = int(len(train_df))
        info["class_distribution_after"] = info["class_distribution_before"]
        return train_df.copy(), info

    if strategy == "undersample":
        target_size = int(original_counts.min())
        replace = False
    else:
        target_size = int(original_counts.max())
        replace = True

    balanced_parts: list[pd.DataFrame] = []
    for class_value in original_counts.index.tolist():
        class_df = train_df[train_df[target_col] == class_value]
        balanced_parts.append(
            class_df.sample(
                n=target_size,
                replace=replace,
                random_state=seed,
            )
        )

    balanced_df = pd.concat(balanced_parts, axis=0)
    balanced_df = balanced_df.sample(frac=1.0, random_state=seed).copy()

    balanced_counts = balanced_df[target_col].value_counts()
    info["rows_after"] = int(len(balanced_df))
    info["class_distribution_after"] = {str(k): int(v) for k, v in balanced_counts.items()}
    return balanced_df, info
