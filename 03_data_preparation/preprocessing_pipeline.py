import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report

rng = np.random.default_rng(12)
n = 240
df = pd.DataFrame({
    "study_hours": rng.normal(5, 1.8, n).clip(0, 10),
    "attendance": rng.uniform(0.4, 1.0, n),
    "study_method": rng.choice(["solo", "group", "mixed"], n),
})
prob = 1 / (1 + np.exp(-(-3.0 + 0.45 * df.study_hours + 2.0 * df.attendance)))
df["passed"] = rng.binomial(1, prob)
df.loc[rng.choice(n, 10, replace=False), "study_hours"] = np.nan

X = df.drop(columns="passed")
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=12, stratify=y
)

numeric = ["study_hours", "attendance"]
categorical = ["study_method"]
numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])
categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])
prep = ColumnTransformer([
    ("numeric", numeric_pipe, numeric),
    ("categorical", categorical_pipe, categorical),
])
model = Pipeline([
    ("preprocess", prep),
    ("classifier", LogisticRegression(max_iter=1000)),
])
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test), zero_division=0))
print("All preprocessing was fitted inside the training pipeline.")
