"""A tiny synthetic supervised-learning experiment."""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Each row has one feature: hours practiced. Target: a synthetic score.
rng = np.random.default_rng(7)
hours = rng.uniform(0, 10, size=120)
scores = 12 + 7.2 * hours + rng.normal(0, 8, size=hours.size)
X = hours.reshape(-1, 1)
y = scores

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(f"Learned slope: {model.coef_[0]:.2f}")
print(f"Learned intercept: {model.intercept_:.2f}")
print(f"Test MAE: {mean_absolute_error(y_test, predictions):.2f} score points")
print("Reminder: this is synthetic data; association is not proof of causation.")
