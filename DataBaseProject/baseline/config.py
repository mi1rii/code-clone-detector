from __future__ import annotations

# aqui centralizamos parametros del baseline para mantener una configuracion clara y reproducible
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BaselineConfig:
    # aqui guardamos rutas y parametros globales que se usan en todo el pipeline
    dataset_root: Path
    metadata_filename: str = "clone_pairs_dataset_metadata.csv"
    seed: int = 42
    train_size: float = 0.7
    val_size: float = 0.15
    test_size: float = 0.15
    imbalance_threshold: float = 1.5

    @property
    def metadata_path(self) -> Path:
        # aqui construimos la ruta completa al csv metadata de entrada
        return self.dataset_root / self.metadata_filename
