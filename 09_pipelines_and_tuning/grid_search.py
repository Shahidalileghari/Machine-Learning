from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=41, stratify=data.target
)
pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression(max_iter=3000)),
])
search = GridSearchCV(
    pipe,
    param_grid={"model__C": [0.01, 0.1, 1.0, 10.0]},
    scoring="f1", cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=41),
    n_jobs=-1,
)
search.fit(X_train, y_train)
print("Best CV F1:", round(search.best_score_, 3))
print("Best parameters:", search.best_params_)
print("Held-out test report:")
print(classification_report(y_test, search.predict(X_test), zero_division=0))
print("Educational data only; this is not a medical tool.")
