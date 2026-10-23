import numpy as np
from sklearn.datasets import load_diabetes, load_breast_cancer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Regression demonstration
reg_data = load_diabetes()
Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    reg_data.data, reg_data.target, test_size=0.2, random_state=42
)
reg = LinearRegression().fit(Xr_train, yr_train)
pred = reg.predict(Xr_test)
print("REGRESSION")
print("MAE:", round(mean_absolute_error(yr_test, pred), 2))
print("R²:", round(r2_score(yr_test, pred), 3))

# Classification demonstration
cls_data = load_breast_cancer()
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    cls_data.data, cls_data.target, test_size=0.2, random_state=42,
    stratify=cls_data.target
)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))
clf.fit(Xc_train, yc_train)
print("\nCLASSIFICATION")
print(classification_report(yc_test, clf.predict(Xc_test),
                            target_names=cls_data.target_names, zero_division=0))
print("Educational demonstration only; do not use this model for diagnosis.")
