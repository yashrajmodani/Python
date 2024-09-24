import pandas as pd


df = pd.read_csv('data.csv')
print(df)
print("===================================")

print(df.head(2))
print("===================================")
print(df.tail(2))
print("===================================")
print(df.info())
print("===================================")
print(df.describe())