import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

print(df.iloc[0:4,0:3 ])

print(df.loc[(df['Age']== 30) & (df['City']=='LA') ])

