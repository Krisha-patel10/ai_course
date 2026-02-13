import pandas as pd
data = pd.read_csv("coffee_shop_sales.csv")

data["total_price"] = data["transaction_qty"] * data["unit_price"]

total_sales = 0
total_sales += data["total_price"]
print(total_sales)
print(data.head())
