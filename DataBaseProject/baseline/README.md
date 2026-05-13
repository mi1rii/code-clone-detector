# Baseline: Clone Detection (Type III / IV)

Pipeline reproducible para:
- Tarea A: `is_clone` (0/1)
- Tarea B: `clone_type` (`type_III` vs `type_IV`) usando solo positivos

Incluye un perfil opcional tipo clase (`--reference-profile`) basado en prácticas de:
- Árboles de decisión
- Métricas por clase + `classification_report`
- Curvas ROC/AUC
- MLP + `GridSearchCV`

## Requisitos

```bash
python -m pip install -r DataBaseProject/baseline/requirements.txt
```

## Ejecución

```bash
python DataBaseProject/run_baseline.py \
  --dataset-root DataBaseProject \
  --metadata-file clone_pairs_dataset_metadata.csv \
  --output-dir DataBaseProject/baseline_outputs \
  --seed 42

# Perfil alineado con prácticas de clase
python DataBaseProject/run_baseline.py \
  --dataset-root DataBaseProject \
  --metadata-file clone_pairs_dataset_metadata.csv \
  --output-dir DataBaseProject/baseline_outputs_reference \
  --seed 42 \
  --reference-profile
```

## Qué hace el pipeline

1. Valida el CSV metadata y limpia filas inválidas.
2. Reconstruye `code_a` y `code_b` desde `file_path` + `snippet_index_a/b`.
3. Preprocesa código (quita comentarios, normaliza espacios).
4. Tokeniza con `tokenize`.
5. Construye features baseline:
   - similitud coseno TF-IDF
   - Jaccard de tokens
   - Dice de tokens
   - overlap de tokens únicos
   - diferencias de longitud, líneas y número de tokens
6. Aplica split por grupos (`problem_id`) para evitar leakage.
7. Entrena y compara:
   - `LogisticRegression`
   - `DecisionTreeClassifier`
   - `MLPClassifier` (opcional)
8. Guarda modelos, métricas, predicciones, matrices de confusión y reporte final.
9. En binario (`is_clone`) genera ROC y AUC cuando hay probabilidades.

## Salidas principales

- `baseline_outputs/datasets/reconstructed_pairs.csv`
- `baseline_outputs/features/task_a/*.csv`
- `baseline_outputs/features/task_b/*.csv`
- `baseline_outputs/task_a_artifacts/**`
- `baseline_outputs/task_b_artifacts/**`
- `baseline_outputs/metrics/*.csv|*.json`
- `baseline_outputs/reports/baseline_report.md`
