# 03 — Data Preparation

A model can only learn from the representation and examples it receives. Data preparation should be driven by the data dictionary and the intended prediction setting—not by blind rules.

## Common operations
- Handle missing values with a reasoned strategy.
- Inspect duplicates and inconsistent units.
- Encode categorical variables.
- Scale features when the algorithm is sensitive to magnitude.
- Split data before learning preprocessing statistics.
- Fit transformations on training data only, then apply them to validation/test data.

## Leakage warning
Leakage occurs when information unavailable at prediction time influences training or evaluation. Examples include fitting a scaler on the full dataset, using a future outcome as a feature, or letting records from the same person appear in both train and test when that would inflate performance.

The example uses a scikit-learn `Pipeline` and `ColumnTransformer`, so preprocessing is fit only on the training partition.
