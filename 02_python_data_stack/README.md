# 02 — Python Data Stack

## Why these tools?
- **NumPy:** efficient arrays and numerical operations.
- **pandas:** labelled tabular data, filtering, joins, aggregation, missing-value inspection.
- **Matplotlib:** plots for understanding distributions and relationships.
- **scikit-learn:** consistent estimator APIs for preprocessing, model fitting, and evaluation.

## First inspection checklist
```python
import pandas as pd

df = pd.read_csv("your_data.csv")
print(df.shape)
print(df.head())
print(df.info())
print(df.describe(include="all"))
print(df.isna().sum().sort_values(ascending=False))
print(df.nunique())
```

Do not assume every numeric column is a meaningful quantity or every identifier is a useful feature. Check units, duplicates, class balance, data collection process, and whether a column would be available at prediction time.
