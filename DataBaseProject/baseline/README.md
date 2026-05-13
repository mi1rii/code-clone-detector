# Baseline: Clone Detection (Type III / IV)

All Python for this pipeline lives in **`DataBaseProject/database_project.ipynb`** (single notebook: build dataset, reconstruct snippets, TF-IDF features, `DecisionTreeClassifier`, metrics, report).

This folder only keeps **`requirements.txt`** for `%pip install -r baseline/requirements.txt` from the notebook.

## Requisitos

```bash
python -m pip install -r DataBaseProject/baseline/requirements.txt
```

## Ejecucion

Open `DataBaseProject/database_project.ipynb` in Jupyter, VS Code, or Google Colab (upload or clone the whole `DataBaseProject` directory, then `%cd` into it on Colab) and **Run all** cells.

## Que hace el pipeline

1. Valida el CSV metadata y limpia filas invalidas.
2. Reconstruye `code_a` y `code_b` desde `file_path` + `snippet_index_a/b`.
3. Preprocesa codigo (quita comentarios, normaliza espacios).
4. Tokeniza con `tokenize`.
5. Construye features baseline:
   - similitud coseno TF-IDF
   - Jaccard de tokens
   - Dice de tokens
   - overlap de tokens unicos
   - diferencias de longitud, lineas y numero de tokens
6. Aplica split por grupos (`problem_id`) para evitar leakage.
7. Entrena y evalua `DecisionTreeClassifier`.
8. Guarda modelo, metricas, predicciones, matriz de confusion y reporte final.
9. En binario (`is_clone`) genera ROC y AUC.

## Salidas principales

- `baseline_outputs/datasets/reconstructed_pairs.csv`
- `baseline_outputs/features/task_a/*.csv`
- `baseline_outputs/features/task_b/*.csv`
- `baseline_outputs/task_a_artifacts/**`
- `baseline_outputs/task_b_artifacts/**`
- `baseline_outputs/metrics/*.csv|*.json`
- `baseline_outputs/reports/baseline_report.md`
