import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("coffee_shop_sales.csv")

data['total_amount'] = data['unit_price'] * data['transaction_qty']

data['transaction_time'] = pd.to_datetime(data['transaction_time'], format='%H:%M:%S')

data['hour'] = data['transaction_time'].dt.hour

average_sales_per_hour = data.groupby('hour')['total_amount'].mean()

plt.plot(average_sales_per_hour.index, average_sales_per_hour.values)

plt.xlabel("Hour of Day")
plt.ylabel("Average Sales")
plt.title("Average Product Sales Per Hour")

plt.show()
