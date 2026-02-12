import pandas as pd 
ed = pd.read_csv("Fintech_user.csv")

print(ed.head(10))
print(ed.tail(15))
print(ed.info(10))
print(ed.describe(10))
