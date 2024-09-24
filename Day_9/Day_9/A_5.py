import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Eva', 'DAn', 'Jojo'],
    'Age': [25, 30, 35, 45, 18, 32],
    'City': ['New york', 'LA', 'Chicago', 'New Jersey', 'India', 'Sri'],
    'Marks': [23.54, 34.45, 32.76, 98.56, 67.65, 54.35]
}
df = pd.DataFrame(data)
# print(df)

# print(df)
#
# # selecting specific columns
# # single columns
# print(df['Name'])
# # selecting multiple columns
# print(df[['Name','Marks']])
# # selecting rows by index position
# print(df.iloc[0])
# # first three rows
# print(df.iloc[:3])
# # specific rows and columns
# print(df.iloc[1:4, [0, 2]])
# # selecting row by index label
# print(df.loc[2])
# # selecting rows with specific condition
# print(df.loc[df['Age'] > 30])
# # selecting specific rowS and columns by labels
# print(df.loc[1:3, ['Name', 'Marks']])
#
# # traditional selection
# # selecting rows where score is greater than 85
# print(df[df['Marks'] > 85])
# # selecting rows where city is either 'Chicago' or 'la'
print(df[df['City'].isin(['Sri', 'India'])])
