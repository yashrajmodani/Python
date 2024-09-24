import pandas as pd

data ={'Values':[1,2,14,10,13,12,12,14,10,13,400]}
df = pd.DataFrame(data)
#
Q1 = df["Values"].quantile(0.25)
print(Q1)

Q3 = df['Values'].quantile(0.75)
print(Q3)

IQR = Q3 - Q1


#Define bounds for Outliers
lower_bound = Q1 - 1.5 *IQR
upper_bound = Q3 + 1.5*IQR

outliers = df[(df['Values'] < lower_bound) | (df['Values']> upper_bound)]
print(outliers)