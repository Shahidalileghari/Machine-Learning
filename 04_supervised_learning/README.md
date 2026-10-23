# 04 — Supervised Learning: Regression and Classification

## Regression
Predicts a numeric quantity. Common metrics include MAE, MSE/RMSE, and R². A useful baseline is often the training-set mean or median.

## Classification
Predicts a class or class probability. Common metrics include precision, recall, F1, ROC-AUC, and a confusion matrix. Accuracy can be misleading with imbalanced classes.

## Algorithm intuition
- **Linear regression:** fits a weighted sum of features for numeric targets.
- **Logistic regression:** maps a linear score through a logistic function to estimate class probability.
- **Decision tree:** learns a sequence of feature-based splits.
- **k-nearest neighbors:** predicts based on nearby training examples.
- **Random forest:** averages many randomized decision trees to reduce variance.

No algorithm is universally best. Choose a simple baseline, validate fairly, and consider data size, feature types, interpretability, latency, and error costs.
