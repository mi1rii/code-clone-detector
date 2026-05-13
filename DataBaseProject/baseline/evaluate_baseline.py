from __future__ import annotations

#calculamos metricas reportes y graficas para evaluar cada modelo del baseline
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)


def evaluate_predictions(
    y_true,
    y_pred,
    labels: list,
) -> dict[str, Any]:
    #calculamos metricas globales y reportes detallados por clase
    acc = accuracy_score(y_true, y_pred)
    precision_macro, recall_macro, f1_macro, _ = precision_recall_fscore_support(
        y_true, y_pred, average="macro", zero_division=0
    )
    precision_weighted, recall_weighted, f1_weighted, _ = precision_recall_fscore_support(
        y_true, y_pred, average="weighted", zero_division=0
    )

    report_dict = classification_report(
        y_true, y_pred, labels=labels, output_dict=True, zero_division=0
    )
    report_text = classification_report(y_true, y_pred, labels=labels, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=labels)

    return {
        "accuracy": float(acc),
        "precision_macro": float(precision_macro),
        "recall_macro": float(recall_macro),
        "f1_macro": float(f1_macro),
        "precision_weighted": float(precision_weighted),
        "recall_weighted": float(recall_weighted),
        "f1_weighted": float(f1_weighted),
        "confusion_matrix": cm.tolist(),
        "classification_report_dict": report_dict,
        "classification_report_text": report_text,
    }


def save_confusion_matrix_plot(
    confusion: np.ndarray,
    labels: list[str],
    title: str,
    output_path: Path,
) -> None:
    #dibujamos y guardamos la matriz de confusion para cada modelo y split
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 5))
    image = ax.imshow(confusion, interpolation="nearest", cmap=plt.cm.Blues)
    ax.figure.colorbar(image, ax=ax)
    ax.set(
        xticks=np.arange(len(labels)),
        yticks=np.arange(len(labels)),
        xticklabels=labels,
        yticklabels=labels,
        ylabel="True label",
        xlabel="Predicted label",
        title=title,
    )
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    #agregamos valores dentro de cada celda para lectura rapida
    threshold = confusion.max() / 2.0 if confusion.size else 0.0
    for i in range(confusion.shape[0]):
        for j in range(confusion.shape[1]):
            ax.text(
                j,
                i,
                format(confusion[i, j], "d"),
                ha="center",
                va="center",
                color="white" if confusion[i, j] > threshold else "black",
            )

    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)


def comparison_table(results: list[dict[str, Any]]) -> pd.DataFrame:
    #armamos una tabla plana para comparar modelos entre tareas y splits
    rows = []
    for result in results:
        rows.append(
            {
                "task": result["task"],
                "model": result["model_name"],
                "split": result["split"],
                "accuracy": result["metrics"]["accuracy"],
                "precision_macro": result["metrics"]["precision_macro"],
                "recall_macro": result["metrics"]["recall_macro"],
                "f1_macro": result["metrics"]["f1_macro"],
                "precision_weighted": result["metrics"]["precision_weighted"],
                "recall_weighted": result["metrics"]["recall_weighted"],
                "f1_weighted": result["metrics"]["f1_weighted"],
            }
        )
    return pd.DataFrame(rows)
