import pandas as pd

df = pd.read_csv("../data/sales_data_usd.csv")
print(df.describe())
