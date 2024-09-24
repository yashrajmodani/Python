#Dataframes
import pandas as pd
import numpy as np
#Creating a dataframe from a dictionary

# data = {
#     'Name': ['Alice','bob','charlie'],
#     'Age': [25,30,35],
#     'city': ['New york','los angeles','chicago']
# }
# df = pd.DataFrame(data)
# print(df)
# # #
# # #Creating a Dataframe form a list of dictionary
# #
# data = [
#     {'Name':'Alice','Age':25,'City':'New york'},
#     {'Name':'Bob','Age':30,'City':'LA'},
#     {'Name':'Charlie','Age':35,'City':'Chicago'},
# ]
# df1 = pd.DataFrame(data)
# print(df1)

# # #Creating dataframes from list
# names = ['Alice','Bob','Charlie']
# ages = [25,30,35]
# city = ['New york','LA','Chicago']
#
# df2 = pd.DataFrame({
#     'Name':names,
#     'AGe':ages,
#     'City':city
# })
# print(df2)
#
# #creating dataframe from numpy array
#
# arr = np.array([[25,'New york'],[30,'LA'],[35,'Chicago']])
# df = pd.DataFrame(arr,columns=['Age','City'])
# print(df)

# #Reading a dataframe from csv file
# df3 = pd.read_csv('dataDemo2')
# print(df3)

# #Cerating dataframe from series
# names = pd.Series(['Alice','Bob','Charlie'],name='Name')
# ages = pd.Series([25,30,35],name="ages")
#
# df4 = pd.concat([names,ages],axis = 1)
# print(df4)

# #sample dataframe
#
data = {
    'Name' :['Alice','Bob','Charlie','Alice','Bob','Charlie'],
    'Age':[25,30,35,25,30,35],
    'City':['New york','LA','Chicago','New york','LA','Chicago'],
    'Marks':[23.54,34.45,32.76,98.56,67.65,54.35]
}
df = pd.DataFrame(data)
df.to_csv('data.csv',index=False)
print(df)
