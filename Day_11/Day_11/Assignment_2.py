
import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
product = np.array(['chocolate', 'Biscuit', 'Coffee', 'Milk', 'Arborvitae'])
sales_a = np.random.randint(50, 500, 12)
sales_b = np.random.randint(50, 500, 12)
sales_c = np.random.randint(50, 500, 12)
sales_d = np.random.randint(50, 500, 12)
sales_e = np.random.randint(50, 500, 12)


# lineplot
plt.figure(figsize=(12, 8))
plt.plot(months, sales_a, label='chocolate', color='green', marker='o', linestyle='-')
plt.plot(months, sales_b, label='Biscuit', color='red', marker="o", linestyle='--')
plt.plot(months, sales_c, label='Coffee', color='purple', marker='o', linestyle='-')
plt.plot(months, sales_d, label='Milk', color='yellow', marker='o', linestyle='-')
plt.plot(months, sales_e, label='Arborvitae', color='black', marker='o', linestyle='--')

# plt.plot(product, sales, label='Dataset2', color='red', marker='s', linestyle='-')
plt.title('Sales data')
plt.xlabel('Months')
plt.ylabel('sales')

plt.legend(loc='upper left')
plt.grid(True)
plt.show()

#bar chart

bar_width = 0.1
bar_positions1 = np.arange(len(months))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width
bar_positions4 = bar_positions3 + bar_width
bar_positions5 = bar_positions4 + bar_width
plt.figure(figsize=(14, 8))


plt.bar(months, sales_a, width=bar_width, label='chocolate', color='skyblue')
plt.bar(bar_positions2, sales_b, width=bar_width, label='Biscuit', color='red')
plt.bar(bar_positions3, sales_c, width=bar_width, label='Coffee', color='orange')
plt.bar(bar_positions4, sales_d, width=bar_width, label='Milk', color='purple')
plt.bar(bar_positions5, sales_e, width=bar_width, label='Arborvitae', color='yellow')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Graph')
plt.legend()
plt.show()
