# Baseline Report

## Dataset Reconstruction
- Metadata input rows: **12484**
- Valid metadata rows after schema cleaning: **12484**
- Reconstructed pairs: **12484**
- Dropped rows: **0**
- Drop reasons: `{}`

## Method
- Pair reconstruction from `file_path` + `snippet_index_a/snippet_index_b`.
- Code preprocessing: comment removal + whitespace normalization.
- Tokenization: Python `tokenize` module.
- Pair features: TF-IDF cosine + lexical/length statistics (Jaccard, Dice, overlap).
- Model used: DecisionTreeClassifier.
- ROC/AUC plots are generated for Task A (`is_clone`).
- Grouped split by `problem_id` to prevent leakage.

## Task A (`is_clone`)
- Balance strategy (train): **oversample**
- Train class distribution before balance: `{'1': 5787, '0': 2967}`
- Train class distribution: `{'1': 5787, '0': 5787}`
- Imbalance ratio (train): **1.0000**
- Best model by validation F1-macro: **decision_tree**
- Best validation F1-macro: **0.8762**

## Task B (`clone_type` on positives)
- Balance strategy (train): **oversample**
- Train class distribution before balance: `{'type_IV': 4037, 'type_III': 1751}`
- Train class distribution: `{'type_III': 4037, 'type_IV': 4037}`
- Imbalance ratio (train): **1.0000**
- Best model by validation F1-macro: **decision_tree**
- Best validation F1-macro: **0.7353**

## Reproducibility
- Random seed: **42**
- Split ratios: train=0.7, val=0.15, test=0.15
