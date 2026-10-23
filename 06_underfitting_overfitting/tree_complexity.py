import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_moons(n_samples=700, noise=0.28, random_state=10)
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=10, stratify=y
)
depths = list(range(1, 16))
train_scores, val_scores = [], []
for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=10)
    model.fit(X_train, y_train)
    train_scores.append(accuracy_score(y_train, model.predict(X_train)))
    val_scores.append(accuracy_score(y_val, model.predict(X_val)))

plt.plot(depths, train_scores, marker="o", label="Train accuracy")
plt.plot(depths, val_scores, marker="o", label="Validation accuracy")
plt.xlabel("Maximum tree depth")
plt.ylabel("Accuracy")
plt.title("Model complexity and generalization")
plt.legend()
plt.tight_layout()
plt.show()
