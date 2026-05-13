from __future__ import annotations

#entrenamos modelos simples y guardamos metricas artefactos y predicciones por tarea
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from .evaluate_baseline import evaluate_predictions, save_confusion_matrix_plot
from .utils import save_json


def _build_models(class_weight, seed: int) -> dict[str, Any]:
    #definimos los dos modelos base que vamos a comparar
    return {
        "logistic_regression": LogisticRegression(
            max_iter=2000,
            solver="liblinear",
            class_weight=class_weight,
            random_state=seed,
        ),
        "decision_tree": DecisionTreeClassifier(
            criterion="gini",
            max_depth=12,
            min_samples_leaf=2,
            class_weight=class_weight,
            random_state=seed,
        ),
    }


def train_and_evaluate_task(
    task_name: str,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    labels: list,
    class_weight,
    output_dir: Path,
    seed: int,
) -> dict[str, Any]:
    #entrenamos y evaluamos ambos modelos sobre val y test
    models = _build_models(class_weight=class_weight, seed=seed)

    #organizamos carpetas de salida por tipo de artefacto
    models_dir = output_dir / "models"
    metrics_dir = output_dir / "metrics"
    plots_dir = output_dir / "plots"
    preds_dir = output_dir / "predictions"
    models_dir.mkdir(parents=True, exist_ok=True)
    metrics_dir.mkdir(parents=True, exist_ok=True)
    plots_dir.mkdir(parents=True, exist_ok=True)
    preds_dir.mkdir(parents=True, exist_ok=True)

    all_results: list[dict[str, Any]] = []
    best_model_name = None
    best_val_f1 = -1.0

    for model_name, model in models.items():
        #ajustamos el modelo con train y lo persistimos en disco
        model.fit(X_train, y_train)
        joblib.dump(model, models_dir / f"{task_name}_{model_name}.joblib")

        model_metrics: dict[str, Any] = {}
        for split_name, (X_split, y_split) in {
            "val": (X_val, y_val),
            "test": (X_test, y_test),
        }.items():
            #predecimos y calculamos metricas por split
            y_pred = model.predict(X_split)
            metrics = evaluate_predictions(y_split, y_pred, labels=labels)
            model_metrics[split_name] = metrics

            #guardamos matriz de confusion como imagen
            cm_array = np.array(metrics["confusion_matrix"])
            save_confusion_matrix_plot(
                confusion=cm_array,
                labels=[str(lbl) for lbl in labels],
                title=f"{task_name} - {model_name} ({split_name})",
                output_path=plots_dir / f"{task_name}_{model_name}_{split_name}_cm.png",
            )

            #exportamos predicciones para auditoria posterior
            pred_df = pd.DataFrame(
                {
                    "row_index": X_split.index,
                    "y_true": y_split.values,
                    "y_pred": y_pred,
                }
            )
            pred_df.to_csv(
                preds_dir / f"{task_name}_{model_name}_{split_name}_predictions.csv",
                index=False,
                encoding="utf-8",
            )

            all_results.append(
                {
                    "task": task_name,
                    "model_name": model_name,
                    "split": split_name,
                    "metrics": metrics,
                }
            )

        #guardamos resumen de metricas por modelo
        save_json(
            model_metrics,
            metrics_dir / f"{task_name}_{model_name}_metrics.json",
        )

        #elegimos el mejor modelo segun f1 macro en validacion
        val_f1 = float(model_metrics["val"]["f1_macro"])
        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            best_model_name = model_name

    if best_model_name is None:
        raise RuntimeError(f"No model could be selected for task {task_name}.")

    #armamos resumen final de la tarea y lo guardamos
    summary = {
        "task": task_name,
        "best_model_by_val_f1_macro": best_model_name,
        "best_val_f1_macro": best_val_f1,
        "class_weight": class_weight,
        "results": all_results,
    }
    save_json(summary, metrics_dir / f"{task_name}_summary.json")
    return summary
