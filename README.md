# Clone baseline (notebook only)

1. Create a venv and install deps: `pip install -r requirements.txt` (plus `jupyter` / `ipykernel` if needed).
2. Open `database_project.ipynb` and select that environment as the kernel.
3. Set the notebook working directory to **this folder** (the repository root), then run all cells.

You need `plagiarism_labels.csv`, `true_semantic_clones/`, and `false_semantic_clones/` here as well (the notebook reads them from disk).
