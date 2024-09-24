import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
print(df.head())
# Scatter plot : Petal Length vs Petal Width
plt.figure(figsize=(8, 6))
sns.scatterplot(x="petal_length", y='petal_width', hue='species', data=df, palette='Set2', s=100)
plt.title('Scatter plot : Petal Length vs Petal Width')
plt.show()

# Box plot: sepal_length vs species
plt.figure(figsize=(8, 8))
sns.boxplot(data=df, x="species", y='sepal_length', hue='species', palette='Set3')
plt.title("#Box plot: sepal_length vs species")
plt.show()

# Violin plot: Petal length vs species
plt.figure(figsize=(8, 8))
sns.violinplot(data=df, x="species", y='petal_length', hue='species', palette='Pastel1')
plt.title("#Violin plot: Petal length vs species")
plt.show()

# pair plot: Relationship bet all features
plt.figure(figsize=(8, 8))
sns.pairplot(df, hue='species', palette='Set1')
plt.suptitle('Pair plot: Iris Dataset', y=1.02)
plt.show()
