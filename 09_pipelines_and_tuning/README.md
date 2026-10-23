# 09 — Pipelines and Hyperparameter Tuning

A pipeline packages preprocessing and an estimator into one object. It reduces accidental inconsistency and makes cross-validation safer.

- **Parameter:** learned from training data, such as regression coefficients.
- **Hyperparameter:** selected by the developer, such as tree depth or regularization strength.
- **Grid search:** evaluates specified combinations using cross-validation.
- **Random search:** samples combinations from a search space.
- **Baseline-first approach:** establish a simple score before spending time tuning.

Keep the final test set untouched until the pipeline and model-selection decisions are complete.
