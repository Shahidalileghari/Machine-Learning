import numpy as np
import pandas as pd

orders = pd.DataFrame({
    "order_date": pd.to_datetime(["2026-01-04", "2026-02-17", "2026-02-28"]),
    "items": [2, 5, 1],
    "subtotal": [1800, 4200, 500],
    "discount": [0.0, 0.10, 0.0],
})
orders["month"] = orders["order_date"].dt.month
orders["weekday"] = orders["order_date"].dt.dayofweek
orders["average_item_price"] = np.where(
    orders["items"] > 0, orders["subtotal"] / orders["items"], np.nan
)
orders["net_subtotal"] = orders["subtotal"] * (1 - orders["discount"])
print(orders)
print("Check whether each engineered feature exists at prediction time.")
