# 06 — Underfitting, Overfitting, and Regularization

- **Underfitting:** model is too limited to capture useful structure; training and validation performance are both poor.
- **Overfitting:** model captures training-specific noise; training performance is much better than validation performance.
- **Generalization gap:** difference between performance on training data and unseen data.
- **Regularization:** constrains model complexity or penalizes large parameters.
- **Bias–variance trade-off:** a useful lens for understanding errors from overly simple versus overly sensitive models.

For decision trees, increasing depth can fit increasingly specific patterns. Use a validation strategy to choose depth; do not select it by repeatedly inspecting test results.
