import numpy as np
import pandas as pd

rng = np.random.default_rng(21)
hours = rng.uniform(1, 8, size=8)
attendance = rng.uniform(0.55, 1.0, size=8)
df = pd.DataFrame({
    "hours_studied": hours.round(1),
    "attendance_rate": attendance.round(2),
})
df["study_band"] = pd.cut(
    df["hours_studied"], bins=[0, 3, 6, 9],
    labels=["low", "medium", "high"], include_lowest=True
)
print(df)
print("\nSummary:")
print(df.describe())
print("\nAverage hours by study band:")
print(df.groupby("study_band", observed=True)["hours_studied"].mean())
