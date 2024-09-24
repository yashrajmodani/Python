import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Eva', 'DAn', 'Jojo'],
    'Age': [25, 30, 35, 45, 18, 32],
    'City': ['New york', 'LA', 'Chicago', 'New Jersey', 'India', 'Sri']
}
df = pd.DataFrame(data)

df['Score'] = [85,90,78,92,88,91]
print(df)
print("===================================")
df['Score'] = df['Score'] +5
print(df)
print("===================================")
df = df.drop('City',axis =1)
print(df)
print("===================================")
#sorted by age

sorted_by_age = df.sort_values(by='Age')
print(sorted_by_age)
print("===================================")
#sorted by index in descending order
sorted_by_index= df.sort_index(ascending=False)
print(sorted_by_index)
print("===================================")
#REname Score to Final Score
df = df.rename(columns={'Score':'Final_Score'})
print(df)
print("===================================")
df_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Eva', 'DAn', 'Jojo'],
    'Age': [25, 30, None, 45,None, 32],
    'Score': [85,90,78,None,88,91]
}

df = pd.DataFrame(df_nan)
print(df)
print("===================================")
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
print("===================================")
df['Score'] = df['Score'].fillna(0)
print(df)
print("===================================")
#Dropping rows with missingg values

print("Original:",df)
df_dropped = df.dropna()
print(df_dropped)
print("===================================")
# #Repalce specific value in the NAme Column
df["Name"] = df['Name'].replace({"Alice":'Mayur','Bob':'Rahul'})
print(df)
# print("===================================")
df['Score'] = df['Score'].replace(0,'N/A')
print(df)