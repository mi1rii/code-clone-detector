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
- Train class distribution: `{'1': 5787, '0': 2967}`
- Imbalance ratio (train): **1.9505**
- Best model by validation F1-macro: **decision_tree**
- Best validation F1-macro: **0.8814**

## Task B (`clone_type` on positives)
- Train class distribution: `{'type_IV': 4037, 'type_III': 1751}`
- Imbalance ratio (train): **2.3055**
- Best model by validation F1-macro: **decision_tree**
- Best validation F1-macro: **0.7555**

## Reproducibility
- Random seed: **42**
- Split ratios: train=0.7, val=0.15, test=0.15
