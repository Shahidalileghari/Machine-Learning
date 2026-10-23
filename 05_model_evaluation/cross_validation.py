from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X, y = data.data, data.target
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
models = {
    "majority baseline": DummyClassifier(strategy="most_frequent"),
    "scaled logistic regression": make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=3000)
    ),
}
for name, model in models.items():
    scores = cross_validate(
        model, X, y, cv=cv,
        scoring={"accuracy": "accuracy", "precision": "precision",
                 "recall": "recall", "f1": "f1"}
    )
    print(f"\n{name}")
    for metric in ("accuracy", "precision", "recall", "f1"):
        values = scores[f"test_{metric}"]
        print(f"{metric}: {values.mean():.3f} ± {values.std():.3f}")
print("Educational dataset only; results are not clinical evidence.")
