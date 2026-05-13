from __future__ import annotations

#orquestamos todo el baseline desde metadata hasta modelos metricas y reporte final
import argparse
import logging
from pathlib import Path

import pandas as pd

from baseline.config import BaselineConfig
from baseline.data_loading import (
    clean_metadata_rows,
    grouped_train_val_test_split,
    load_metadata_csv,
    split_statistics,
    validate_metadata_schema,
)
from baseline.evaluate_baseline import comparison_table
from baseline.feature_extraction import (
    build_pair_features,
    fit_tfidf_vectorizer,
    prepare_pair_text_fields,
    save_feature_splits,
)
from baseline.snippet_reconstruction import reconstruct_pairs_from_metadata
from baseline.train_baseline import train_and_evaluate_task
from baseline.utils import (
    class_distribution,
    ensure_dir,
    imbalance_ratio,
    save_json,
    set_global_seed,
    setup_logging,
)


def assign_split_column(
    df: pd.DataFrame,
    train_idx: pd.Index,
    val_idx: pd.Index,
    test_idx: pd.Index,
    split_col: str,
) -> pd.DataFrame:
    #etiquetamos cada fila como train val o test a partir de indices ya agrupados
    result = df.copy()
    result[split_col] = "unassigned"
    result.loc[train_idx, split_col] = "train"
    result.loc[val_idx, split_col] = "val"
    result.loc[test_idx, split_col] = "test"
    return result


def _log_split_stats(logger: logging.Logger, title: str, stats: list[dict]) -> None:
    #dejamos en logs una vista clara de filas grupos y clases por split
    logger.info(title)
    for row in stats:
        logger.info(
            "  %s | rows=%s | unique_problem_id=%s | class_dist=%s",
            row["split"],
            row["rows"],
            row["unique_groups"],
            row["class_distribution"],
        )


def _train_task_a(
    prepared_df: pd.DataFrame,
    config: BaselineConfig,
    output_dir: Path,
    logger: logging.Logger,
) -> dict:
    #entrenamos la tarea binaria clone vs non clone
    split = grouped_train_val_test_split(
        df=prepared_df,
        group_col="problem_id",
        target_col="is_clone",
        seed=config.seed,
        train_size=config.train_size,
        val_size=config.val_size,
        test_size=config.test_size,
    )
    task_df = assign_split_column(
        prepared_df,
        train_idx=split.train_idx,
        val_idx=split.val_idx,
        test_idx=split.test_idx,
        split_col="split_task_a",
    )
    task_df.to_csv(output_dir / "datasets" / "task_a_reconstructed_with_split.csv", index=False)

    #reportamos estadisticas del split para verificar ausencia de leakage
    stats = split_statistics(
        task_df, split_col="split_task_a", target_col="is_clone", group_col="problem_id"
    )
    _log_split_stats(logger, "Task A split statistics (`is_clone`):", stats)
    save_json({"split_stats": stats}, output_dir / "metrics" / "task_a_split_stats.json")

    #separamos dataframes por split
    train_df = task_df[task_df["split_task_a"] == "train"].copy()
    val_df = task_df[task_df["split_task_a"] == "val"].copy()
    test_df = task_df[task_df["split_task_a"] == "test"].copy()

    #aplicamos class_weight balanced cuando el desbalance supera el umbral definido
    ratio = imbalance_ratio(train_df["is_clone"])
    class_weight = "balanced" if ratio >= config.imbalance_threshold else None
    logger.info(
        "Task A class imbalance ratio (train): %.4f | class_weight=%s",
        ratio,
        class_weight,
    )

    #ajustamos tf idf con train y construimos features en train val y test
    vectorizer = fit_tfidf_vectorizer(train_df)
    features_train = build_pair_features(train_df, vectorizer)
    features_val = build_pair_features(val_df, vectorizer)
    features_test = build_pair_features(test_df, vectorizer)

    #exportamos features del baseline para reproducibilidad experimental
    save_feature_splits(
        split_to_features={
            "train": features_train,
            "val": features_val,
            "test": features_test,
        },
        split_to_targets={
            "train": train_df["is_clone"],
            "val": val_df["is_clone"],
            "test": test_df["is_clone"],
        },
        output_dir=output_dir / "features" / "task_a",
        target_name="is_clone",
    )

    #entrenamos y evaluamos el baseline unicamente con decision tree
    summary = train_and_evaluate_task(
        task_name="is_clone",
        X_train=features_train,
        y_train=train_df["is_clone"],
        X_val=features_val,
        y_val=val_df["is_clone"],
        X_test=features_test,
        y_test=test_df["is_clone"],
        labels=[0, 1],
        class_weight=class_weight,
        output_dir=output_dir / "task_a_artifacts",
        seed=config.seed,
        save_roc_curves=True,
    )
    summary["class_imbalance_ratio_train"] = ratio
    summary["class_distribution_train"] = class_distribution(train_df["is_clone"])
    return summary


def _train_task_b(
    prepared_df: pd.DataFrame,
    config: BaselineConfig,
    output_dir: Path,
    logger: logging.Logger,
) -> dict:
    #entrenamos la tarea multiclasica solo en positivos para distinguir type_iii y type_iv
    positives_df = prepared_df[prepared_df["is_clone"] == 1].copy()
    split = grouped_train_val_test_split(
        df=positives_df,
        group_col="problem_id",
        target_col="clone_type",
        seed=config.seed + 100,
        train_size=config.train_size,
        val_size=config.val_size,
        test_size=config.test_size,
    )
    task_df = assign_split_column(
        positives_df,
        train_idx=split.train_idx,
        val_idx=split.val_idx,
        test_idx=split.test_idx,
        split_col="split_task_b",
    )
    task_df.to_csv(output_dir / "datasets" / "task_b_positive_with_split.csv", index=False)

    #revisamos que la distribucion por split sea razonable
    stats = split_statistics(
        task_df, split_col="split_task_b", target_col="clone_type", group_col="problem_id"
    )
    _log_split_stats(logger, "Task B split statistics (`clone_type` in positives):", stats)
    save_json({"split_stats": stats}, output_dir / "metrics" / "task_b_split_stats.json")

    #separamos dataframes por split
    train_df = task_df[task_df["split_task_b"] == "train"].copy()
    val_df = task_df[task_df["split_task_b"] == "val"].copy()
    test_df = task_df[task_df["split_task_b"] == "test"].copy()

    #decidimos si usar class_weight balanced para compensar desbalance
    ratio = imbalance_ratio(train_df["clone_type"])
    class_weight = "balanced" if ratio >= config.imbalance_threshold else None
    logger.info(
        "Task B class imbalance ratio (train): %.4f | class_weight=%s",
        ratio,
        class_weight,
    )

    #vectorizamos y creamos features del par para los tres splits
    vectorizer = fit_tfidf_vectorizer(train_df)
    features_train = build_pair_features(train_df, vectorizer)
    features_val = build_pair_features(val_df, vectorizer)
    features_test = build_pair_features(test_df, vectorizer)

    #guardamos features para trazabilidad
    save_feature_splits(
        split_to_features={
            "train": features_train,
            "val": features_val,
            "test": features_test,
        },
        split_to_targets={
            "train": train_df["clone_type"],
            "val": val_df["clone_type"],
            "test": test_df["clone_type"],
        },
        output_dir=output_dir / "features" / "task_b",
        target_name="clone_type",
    )

    #ejecutamos entrenamiento y evaluacion con ambas familias de modelo
    labels = sorted(task_df["clone_type"].unique().tolist())
    summary = train_and_evaluate_task(
        task_name="clone_type",
        X_train=features_train,
        y_train=train_df["clone_type"],
        X_val=features_val,
        y_val=val_df["clone_type"],
        X_test=features_test,
        y_test=test_df["clone_type"],
        labels=labels,
        class_weight=class_weight,
        output_dir=output_dir / "task_b_artifacts",
        seed=config.seed,
    )
    summary["class_imbalance_ratio_train"] = ratio
    summary["class_distribution_train"] = class_distribution(train_df["clone_type"])
    return summary


def _build_markdown_report(
    output_path: Path,
    config: BaselineConfig,
    metadata_rows: int,
    cleaned_rows: int,
    reconstructed_rows: int,
    dropped_rows: int,
    drop_reasons: dict,
    task_a_summary: dict,
    task_b_summary: dict,
) -> None:
    #dejamos un reporte breve y legible con datos de reconstruccion y rendimiento
    model_lines = [
        "- Model used: DecisionTreeClassifier.",
    ]
    model_lines.append("- ROC/AUC plots are generated for Task A (`is_clone`).")

    lines = [
        "# Baseline Report",
        "",
        "## Dataset Reconstruction",
        f"- Metadata input rows: **{metadata_rows}**",
        f"- Valid metadata rows after schema cleaning: **{cleaned_rows}**",
        f"- Reconstructed pairs: **{reconstructed_rows}**",
        f"- Dropped rows: **{dropped_rows}**",
        f"- Drop reasons: `{drop_reasons}`",
        "",
        "## Method",
        "- Pair reconstruction from `file_path` + `snippet_index_a/snippet_index_b`.",
        "- Code preprocessing: comment removal + whitespace normalization.",
        "- Tokenization: Python `tokenize` module.",
        "- Pair features: TF-IDF cosine + lexical/length statistics (Jaccard, Dice, overlap).",
        *model_lines,
        "- Grouped split by `problem_id` to prevent leakage.",
        "",
        "## Task A (`is_clone`)",
        f"- Train class distribution: `{task_a_summary.get('class_distribution_train', {})}`",
        f"- Imbalance ratio (train): **{task_a_summary.get('class_imbalance_ratio_train', 0):.4f}**",
        f"- Best model by validation F1-macro: **{task_a_summary['best_model_by_val_f1_macro']}**",
        f"- Best validation F1-macro: **{task_a_summary['best_val_f1_macro']:.4f}**",
        "",
        "## Task B (`clone_type` on positives)",
        f"- Train class distribution: `{task_b_summary.get('class_distribution_train', {})}`",
        f"- Imbalance ratio (train): **{task_b_summary.get('class_imbalance_ratio_train', 0):.4f}**",
        f"- Best model by validation F1-macro: **{task_b_summary['best_model_by_val_f1_macro']}**",
        f"- Best validation F1-macro: **{task_b_summary['best_val_f1_macro']:.4f}**",
        "",
        "## Reproducibility",
        f"- Random seed: **{config.seed}**",
        f"- Split ratios: train={config.train_size}, val={config.val_size}, test={config.test_size}",
        "",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    #definimos argumentos para ejecutar el pipeline en distintos entornos
    parser = argparse.ArgumentParser(description="Run lexical TF-IDF baseline for clone detection.")
    parser.add_argument(
        "--dataset-root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Dataset root containing metadata CSV and clone folders.",
    )
    parser.add_argument(
        "--metadata-file",
        type=str,
        default="clone_pairs_dataset_metadata.csv",
        help="Metadata CSV filename.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "baseline_outputs",
        help="Directory to store datasets, features, models, and reports.",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    parser.add_argument(
        "--imbalance-threshold",
        type=float,
        default=1.5,
        help="If max/min class ratio in train >= threshold, use class_weight='balanced'.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="decision_tree",
        choices=["decision_tree"],
        help="Baseline model. This pipeline uses DecisionTreeClassifier only.",
    )
    args = parser.parse_args()

    #consolidamos configuracion de la corrida
    config = BaselineConfig(
        dataset_root=args.dataset_root,
        metadata_filename=args.metadata_file,
        seed=args.seed,
        imbalance_threshold=args.imbalance_threshold,
    )

    #creamos estructura base de carpetas de salida
    output_dir = ensure_dir(args.output_dir)
    ensure_dir(output_dir / "datasets")
    ensure_dir(output_dir / "metrics")
    ensure_dir(output_dir / "features")
    ensure_dir(output_dir / "reports")

    #preparamos logs y semilla global
    logger = setup_logging(output_dir / "run.log")
    set_global_seed(config.seed)
    logger.info("Starting baseline pipeline.")
    logger.info("Dataset root: %s", config.dataset_root)
    logger.info("Metadata CSV: %s", config.metadata_path)
    logger.info("Model configuration: decision_tree only")

    #cargamos metadata y verificamos su esquema
    metadata_df = load_metadata_csv(config.metadata_path)
    metadata_rows = len(metadata_df)
    logger.info("Loaded metadata rows: %d", metadata_rows)

    schema_ok, schema_errors = validate_metadata_schema(metadata_df)
    if not schema_ok:
        for err in schema_errors:
            logger.error(err)
        raise ValueError("Metadata schema validation failed.")

    #limpiamos metadata y eliminamos filas con valores invalidos
    cleaned_metadata_df, invalid_metadata_df = clean_metadata_rows(metadata_df)
    logger.info(
        "Metadata cleaning: valid_rows=%d | invalid_rows=%d",
        len(cleaned_metadata_df),
        len(invalid_metadata_df),
    )

    #reconstruimos code_a code_b desde los archivos fuente
    reconstructed_df, dropped_df, reconstruction_summary = reconstruct_pairs_from_metadata(
        cleaned_metadata_df, dataset_root=config.dataset_root
    )
    logger.info("Reconstruction summary: %s", reconstruction_summary)

    #unificamos descartes de metadata y descartes de reconstruccion
    if not invalid_metadata_df.empty:
        dropped_df = pd.concat([dropped_df, invalid_metadata_df], ignore_index=True, sort=False)

    #guardamos datasets de trabajo y auditoria
    reconstructed_path = output_dir / "datasets" / "reconstructed_pairs.csv"
    dropped_path = output_dir / "datasets" / "dropped_rows.csv"
    reconstructed_df.to_csv(reconstructed_path, index=False, encoding="utf-8")
    dropped_df.to_csv(dropped_path, index=False, encoding="utf-8")

    logger.info("Saved reconstructed dataset: %s", reconstructed_path)
    logger.info("Saved dropped rows dataset: %s", dropped_path)

    #preprocesamos codigo y tokens antes de extraer features
    prepared_df = prepare_pair_text_fields(reconstructed_df)
    prepared_df.to_csv(
        output_dir / "datasets" / "reconstructed_pairs_preprocessed.csv",
        index=False,
        encoding="utf-8",
    )
    logger.info("Preprocessing completed on %d rows.", len(prepared_df))

    #entrenamos ambas tareas del baseline
    task_a_summary = _train_task_a(
        prepared_df,
        config=config,
        output_dir=output_dir,
        logger=logger,
    )
    task_b_summary = _train_task_b(
        prepared_df,
        config=config,
        output_dir=output_dir,
        logger=logger,
    )

    #generamos tablas comparativas por tarea y consolidado
    task_a_comp = comparison_table(task_a_summary["results"])
    task_b_comp = comparison_table(task_b_summary["results"])
    task_a_comp.to_csv(output_dir / "metrics" / "task_a_model_comparison.csv", index=False)
    task_b_comp.to_csv(output_dir / "metrics" / "task_b_model_comparison.csv", index=False)
    combined_comp = pd.concat([task_a_comp, task_b_comp], ignore_index=True)
    combined_comp.to_csv(output_dir / "metrics" / "all_tasks_model_comparison.csv", index=False)

    #guardamos resumenes json por tarea
    save_json(task_a_summary, output_dir / "metrics" / "task_a_summary.json")
    save_json(task_b_summary, output_dir / "metrics" / "task_b_summary.json")

    #escribimos reporte final en markdown
    _build_markdown_report(
        output_path=output_dir / "reports" / "baseline_report.md",
        config=config,
        metadata_rows=metadata_rows,
        cleaned_rows=len(cleaned_metadata_df),
        reconstructed_rows=len(reconstructed_df),
        dropped_rows=len(dropped_df),
        drop_reasons=(dropped_df["drop_reason"].value_counts().to_dict() if not dropped_df.empty else {}),
        task_a_summary=task_a_summary,
        task_b_summary=task_b_summary,
    )
    logger.info("Baseline report saved to %s", output_dir / "reports" / "baseline_report.md")
    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    #ejecutamos el pipeline completo cuando corremos este archivo directo
    main()
