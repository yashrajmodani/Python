# data visualization
# simplifies complex data,reveals hidden insights, facilitates decision-making and enhances communication

# matplotlib is a python library for creating visualizations
# steps to create a graph:
# 1.prepare the data, 2.create a plot, 3.customize the plot, 4.display or savethe plot

# graph types:
# line plots, bar charts, scatter plots, histograms, pie charts


import matplotlib.pyplot as plt
import numpy as np
import random
x = np.arange(10)
print(x)
y = np.random.rand(10)
print(y)
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bakchodi')
plt.show()
