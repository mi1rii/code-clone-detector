#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd


def _add_src_to_path(dataset_dir: Path) -> None:
    src = dataset_dir / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))


def _df_to_markdown(df: pd.DataFrame) -> str:
    try:
        return df.to_markdown(index=False)
    except Exception:
        header = "| " + " | ".join(df.columns.tolist()) + " |"
        sep = "| " + " | ".join(["---"] * len(df.columns)) + " |"
        rows = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(x) for x in row.tolist()) + " |")
        return "\n".join([header, sep] + rows)


def _run() -> None:
    parser = argparse.ArgumentParser(
        description="Compara baseline lexical vs baseline+features Baker para clasificacion de tipo de clon."
    )
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--estrategia-balanceo", default="undersample", choices=["none", "undersample", "oversample"])
    parser.add_argument("--min-match-len", type=int, default=3)
    args = parser.parse_args()

    dataset_dir = args.dataset_dir.resolve()
    _add_src_to_path(dataset_dir)

    from baseline_pipeline import (  # pylint: disable=import-outside-toplevel
        ajustar_tfidf,
        asignar_split,
        construir_features_par,
        cargar_metadata,
        entrenar_evaluar_decision_tree,
        estadisticas_split,
        limpiar_metadata,
        preparar_campos_par,
        reconstruir_pares,
        split_por_grupo,
    )

    reports_dir = dataset_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    ruta_metadata = dataset_dir / "clone_pairs_dataset_metadata.csv"
    df_meta = cargar_metadata(ruta_metadata)
    df_meta = limpiar_metadata(df_meta)

    df_pairs, df_drop, resumen = reconstruir_pares(df_meta, dataset_dir)
    if len(df_drop) > 0:
        print("[warn] filas descartadas en reconstruccion:", len(df_drop))
    print("[info] resumen reconstruccion:", resumen)

    df_prep = preparar_campos_par(df_pairs)

    split = split_por_grupo(
        df=df_prep,
        group_col="problem_id",
        target_col="clone_type",
        seed=args.seed + 100,
        train_size=0.7,
        val_size=0.15,
        test_size=0.15,
    )
    df_task = asignar_split(df_prep, split.train_idx, split.val_idx, split.test_idx)

    print("[info] estadisticas split:")
    for row in estadisticas_split(df_task, "split", "clone_type", "problem_id"):
        print(row)

    etiquetas_multi = sorted(df_task["clone_type"].unique().tolist())
    etiquetas_bin = sorted(df_task["clone_family_bin"].unique().tolist())

    res_base_multi = entrenar_evaluar_decision_tree(
        df_task,
        columna_target="clone_type",
        etiquetas=etiquetas_multi,
        seed=args.seed + 100,
        estrategia_balanceo=args.estrategia_balanceo,
        incluir_baker=False,
        min_match_len=args.min_match_len,
    )
    res_baker_multi = entrenar_evaluar_decision_tree(
        df_task,
        columna_target="clone_type",
        etiquetas=etiquetas_multi,
        seed=args.seed + 100,
        estrategia_balanceo=args.estrategia_balanceo,
        incluir_baker=True,
        min_match_len=args.min_match_len,
    )

    res_base_bin = entrenar_evaluar_decision_tree(
        df_task,
        columna_target="clone_family_bin",
        etiquetas=etiquetas_bin,
        seed=args.seed + 100,
        estrategia_balanceo=args.estrategia_balanceo,
        incluir_baker=False,
        min_match_len=args.min_match_len,
    )
    res_baker_bin = entrenar_evaluar_decision_tree(
        df_task,
        columna_target="clone_family_bin",
        etiquetas=etiquetas_bin,
        seed=args.seed + 100,
        estrategia_balanceo=args.estrategia_balanceo,
        incluir_baker=True,
        min_match_len=args.min_match_len,
    )

    # Export feature dataset using train-fitted TF-IDF to avoid leakage.
    df_train = df_task[df_task["split"] == "train"].copy()
    df_val = df_task[df_task["split"] == "val"].copy()
    df_test = df_task[df_task["split"] == "test"].copy()
    vector = ajustar_tfidf(df_train)
    x_train = construir_features_par(df_train, vector, incluir_baker=True, min_match_len=args.min_match_len)
    x_val = construir_features_par(df_val, vector, incluir_baker=True, min_match_len=args.min_match_len)
    x_test = construir_features_par(df_test, vector, incluir_baker=True, min_match_len=args.min_match_len)
    x_all = pd.concat([x_train, x_val, x_test], axis=0).sort_index()
    meta_cols = df_task[["problem_id", "clone_type", "clone_family_bin", "split"]].copy()
    df_features_export = pd.concat([meta_cols, x_all], axis=1)

    summary_rows = [
        {
            "task": "clone_type_4class",
            "variant": "baseline",
            "num_features": res_base_multi["num_features"],
            "accuracy_val": res_base_multi["metricas_val"]["accuracy"],
            "f1_macro_val": res_base_multi["metricas_val"]["f1_macro"],
            "accuracy_test": res_base_multi["metricas_test"]["accuracy"],
            "f1_macro_test": res_base_multi["metricas_test"]["f1_macro"],
        },
        {
            "task": "clone_type_4class",
            "variant": "baseline_plus_baker",
            "num_features": res_baker_multi["num_features"],
            "accuracy_val": res_baker_multi["metricas_val"]["accuracy"],
            "f1_macro_val": res_baker_multi["metricas_val"]["f1_macro"],
            "accuracy_test": res_baker_multi["metricas_test"]["accuracy"],
            "f1_macro_test": res_baker_multi["metricas_test"]["f1_macro"],
        },
        {
            "task": "clone_family_binary",
            "variant": "baseline",
            "num_features": res_base_bin["num_features"],
            "accuracy_val": res_base_bin["metricas_val"]["accuracy"],
            "f1_macro_val": res_base_bin["metricas_val"]["f1_macro"],
            "accuracy_test": res_base_bin["metricas_test"]["accuracy"],
            "f1_macro_test": res_base_bin["metricas_test"]["f1_macro"],
        },
        {
            "task": "clone_family_binary",
            "variant": "baseline_plus_baker",
            "num_features": res_baker_bin["num_features"],
            "accuracy_val": res_baker_bin["metricas_val"]["accuracy"],
            "f1_macro_val": res_baker_bin["metricas_val"]["f1_macro"],
            "accuracy_test": res_baker_bin["metricas_test"]["accuracy"],
            "f1_macro_test": res_baker_bin["metricas_test"]["f1_macro"],
        },
    ]
    df_summary = pd.DataFrame(summary_rows)

    # Per-class comparison for multi-class task (TEST).
    rep_base = res_base_multi["metricas_test"]["classification_report_dict"]
    rep_baker = res_baker_multi["metricas_test"]["classification_report_dict"]
    per_class_rows = []
    for label in etiquetas_multi:
        per_class_rows.append(
            {
                "label": label,
                "f1_baseline": rep_base[label]["f1-score"],
                "f1_baker": rep_baker[label]["f1-score"],
                "delta_f1": rep_baker[label]["f1-score"] - rep_base[label]["f1-score"],
                "precision_baseline": rep_base[label]["precision"],
                "precision_baker": rep_baker[label]["precision"],
                "recall_baseline": rep_base[label]["recall"],
                "recall_baker": rep_baker[label]["recall"],
            }
        )
    df_class = pd.DataFrame(per_class_rows).sort_values("label")

    out_summary_csv = reports_dir / "baseline_vs_baker_summary.csv"
    out_class_csv = reports_dir / "baseline_vs_baker_per_class.csv"
    out_features_csv = reports_dir / "features_baseline_plus_baker.csv"
    out_json = reports_dir / "baseline_vs_baker_raw_metrics.json"
    out_md = reports_dir / "baseline_vs_baker_report.md"
    df_summary.to_csv(out_summary_csv, index=False, encoding="utf-8")
    df_class.to_csv(out_class_csv, index=False, encoding="utf-8")
    df_features_export.to_csv(out_features_csv, index=False, encoding="utf-8")

    def _strip_model(payload: dict) -> dict:
        out = dict(payload)
        out.pop("modelo", None)
        return out

    raw = {
        "multi_baseline": _strip_model(res_base_multi),
        "multi_baker": _strip_model(res_baker_multi),
        "binary_baseline": _strip_model(res_base_bin),
        "binary_baker": _strip_model(res_baker_bin),
        "split_rows": estadisticas_split(df_task, "split", "clone_type", "problem_id"),
        "reconstruction_summary": resumen,
        "min_match_len": args.min_match_len,
    }
    out_json.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")

    acc_delta = (
        res_baker_multi["metricas_test"]["accuracy"] - res_base_multi["metricas_test"]["accuracy"]
    )
    f1m_delta = (
        res_baker_multi["metricas_test"]["f1_macro"] - res_base_multi["metricas_test"]["f1_macro"]
    )
    row_t3 = df_class[df_class["label"] == "type_III"].iloc[0].to_dict()
    row_t4 = df_class[df_class["label"] == "type_IV"].iloc[0].to_dict()

    md = []
    md.append("# Reporte baseline vs baseline + Baker")
    md.append("")
    md.append("## Resumen")
    md.append(f"- Split por grupo (`problem_id`) mantenido con `seed={args.seed + 100}`.")
    md.append(f"- Estrategia de balanceo en entrenamiento: `{args.estrategia_balanceo}`.")
    md.append(f"- Baker `min_match_len={args.min_match_len}`.")
    md.append("")
    md.append("## Tabla comparativa (principal)")
    md.append(_df_to_markdown(df_summary))
    md.append("")
    md.append("## Comparacion por clase (TEST, 4 clases)")
    md.append(_df_to_markdown(df_class))
    md.append("")
    md.append("## Interpretacion rapida")
    md.append(f"- Delta accuracy TEST (4 clases): `{acc_delta:+.6f}`.")
    md.append(f"- Delta F1 macro TEST (4 clases): `{f1m_delta:+.6f}`.")
    md.append(
        f"- `type_III` delta F1: `{row_t3['delta_f1']:+.6f}` (baseline `{row_t3['f1_baseline']:.6f}` -> baker `{row_t3['f1_baker']:.6f}`)."
    )
    md.append(
        f"- `type_IV` delta F1: `{row_t4['delta_f1']:+.6f}` (baseline `{row_t4['f1_baseline']:.6f}` -> baker `{row_t4['f1_baker']:.6f}`)."
    )
    md.append("")
    md.append("## Artefactos")
    md.append(f"- `{out_summary_csv.name}`")
    md.append(f"- `{out_class_csv.name}`")
    md.append(f"- `{out_features_csv.name}`")
    md.append(f"- `{out_json.name}`")
    out_md.write_text("\n".join(md), encoding="utf-8")

    print("\n[ok] Resumen comparativo:")
    print(df_summary.to_string(index=False))
    print("\n[ok] Comparacion por clase (TEST):")
    print(df_class.to_string(index=False))
    print("\n[ok] Reportes guardados en:", reports_dir)


if __name__ == "__main__":
    _run()
