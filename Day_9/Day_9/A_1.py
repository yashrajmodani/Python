import pandas as pd

# creating a series from list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

# sum function
print(series.sum())

# filtering values greater than 10
print("values greater than 10 \n ", series[series > 10])

#creating a series with the custom index
series3 = pd.Series(data, index=['a','b','c','d','e'])
print(series3)

# creating a series from dictionary
data_dict = {'apple': 43, 'banana': 4, 'cherry': 66}
series1 = pd.Series(data_dict)
print(series1)

# creating a series from scalar value
series2 = pd.Series(10, index=['a', 'b', 'c'])
print(series2)
#accesing by position
print(series2[1])

#accessing by index
print(series2['b'])
