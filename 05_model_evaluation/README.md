# 05 — Model Evaluation

## Split roles
- **Training set:** fit model parameters.
- **Validation set / cross-validation:** choose features, model family, and hyperparameters.
- **Test set:** final, limited-use estimate after decisions are complete.

A common beginner mistake is repeatedly checking the test set and adjusting the model to it. That turns the test set into part of the development process.

## Metric choice
- **MAE:** average absolute error; easy to interpret in target units.
- **RMSE:** penalizes large errors more strongly.
- **Precision:** among predicted positives, how many are positive?
- **Recall:** among actual positives, how many were found?
- **F1:** harmonic mean of precision and recall.
- **ROC-AUC:** ranking quality across thresholds; does not itself choose a threshold.
- **Confusion matrix:** counts true/false positives and negatives.

Always compare against a baseline and explain why the selected metric matches the use case.
