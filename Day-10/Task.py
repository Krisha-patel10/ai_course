import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("coffee_shop_sales.csv")

# 1. Add total_amount column
data['total_amount'] = data['unit_price'] * data['transaction_qty']

# 2. Convert transaction_time column to datetime
data['transaction_time'] = pd.to_datetime(data['transaction_time'])

# 3. Extract hour
data['hour'] = data['transaction_time'].dt.hour

# 4. Calculate average sales per hour
average_sales_per_hour = data.groupby('hour')['total_amount'].mean()

# 5. Plot graph
plt.figure()
plt.plot(average_sales_per_hour.index, average_sales_per_hour.values)

plt.xlabel("Hour of Day")
plt.ylabel("Average Sales")
plt.title("Average Product Sales Per Hour")

plt.show()
