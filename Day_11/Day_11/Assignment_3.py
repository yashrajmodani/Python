
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    "Months": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    "Sub-Group": ["X", "X", "Y", "X", "Y", "Y", "X", "Y", "Y", "Y", "Y", "Y"],
    "Sales": np.random.randint(50, 500,size=12)
})

plt.figure(figsize=(8, 6))
sns.lineplot(x='Months', y='Sales', data=df)
plt.title('Line plot : Months v/s Sales')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Months', y='Sales', data=df)
plt.title('Bar plot : Months v/s Sales')
plt.show()

Months= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Sales= np.random.randint(50, 500,size=12)

plt.figure(figsize=(8, 6))
plt.pie(Sales, labels=Months, autopct='%1.1f%%',counterclock=False)
plt.title('Pie chart : Months v/s Sales')
plt.show()


df_melted = pd.melt(df, id_vars=['Months'], value_vars=['Sales'], var_name='Type', value_name='Value')
plt.figure(figsize=(8, 8))
plt.title("Violin plot: Months vs sales")
sns.violinplot(x='Months',  y='Sales', data=df_melted,hue='Type')

plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()


