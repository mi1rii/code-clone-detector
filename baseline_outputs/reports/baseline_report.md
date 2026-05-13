# Clone Detection Baseline Report

## Summary
- Seed: 42
- Imbalance threshold: 1.5
- Balance strategy: undersample

## Model Comparison

```
  task         model split  accuracy  precision_macro  recall_macro  f1_macro  precision_weighted  recall_weighted  f1_weighted
task_a decision_tree   val  0.880876         0.859680      0.893429  0.870707            0.895845         0.880876     0.883530
task_a decision_tree  test  0.885272         0.868725      0.899009  0.877950            0.899946         0.885272     0.887521
task_b decision_tree   val  1.000000         1.000000      1.000000  1.000000            1.000000         1.000000     1.000000
task_b decision_tree  test  1.000000         1.000000      1.000000  1.000000            1.000000         1.000000     1.000000
```
