from __future__ import annotations

#reunimos utilidades simples para crear carpetas, logs y archivos de salida del baseline
import json
import logging
import random
from pathlib import Path
from typing import Any

import numpy as np


def ensure_dir(path: Path) -> Path:
    #nos aseguramos de que la carpeta exista antes de guardar resultados
    path.mkdir(parents=True, exist_ok=True)
    return path


def setup_logging(log_path: Path) -> logging.Logger:
    #preparamos un logger con salida a archivo y a consola para trazabilidad
    ensure_dir(log_path.parent)
    logger = logging.getLogger("clone_baseline")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    #definimos un formato legible para ver fecha, nivel y mensaje
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    #conectamos el archivo de log principal de la corrida
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    #conectamos tambien consola para seguimiento en tiempo real
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def set_global_seed(seed: int) -> None:
    #fijamos semillas para que los resultados sean reproducibles
    random.seed(seed)
    np.random.seed(seed)


def save_json(payload: dict[str, Any], output_path: Path) -> None:
    #guardamos diccionarios en json de forma consistente
    ensure_dir(output_path.parent)
    with output_path.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2, ensure_ascii=False)


def class_distribution(series) -> dict[str, int]:
    #calculamos distribucion de clases para reportes y control de desbalance
    counts = series.value_counts(dropna=False)
    return {str(k): int(v) for k, v in counts.items()}


def imbalance_ratio(series) -> float:
    #medimos que tan desbalanceada esta una variable objetivo
    counts = series.value_counts()
    if counts.empty:
        return 1.0
    if len(counts) == 1:
        return float("inf")
    return float(counts.max() / counts.min())
