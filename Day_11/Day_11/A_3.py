import matplotlib.pyplot as plt
import numpy as np

x= np.arange(1,11)
y1=np.array([1,3,4,7,9,12,15,18,19,22])
y2=np.array([2,5,7,10,12,13,16,18,21,23])

# #creating subplots
fig, axs = plt.subplots(2,2,figsize =(12,10))#2X2 GRID SIXE OF THE PLOT


# #1.line plot

plt.figure(figsize=(8,6))
plt.plot(x,y1,label = 'Dataset1',color = 'blue', marker = 'o',linestyle = '--')
plt.plot(x,y2,label = 'Dataset2',color = 'red', marker = 's',linestyle = '-')
plt.title('Line plot example')
plt.xlabel('x-axix')
plt.ylabel('y-axix')

plt.legend()
plt.grid(True)
plt.show()

# 2.bar chart
categories = ['category A','category B','category C','category D']
values = [4,7,1,8]
plt.figure(figsize=(8,6))
plt.bar(categories,values,color = 'orange')
plt.title('Bar Chart example')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()


# scatter plot
#
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title('Scatter plot example')
plt.xlabel('X axis')
plt.ylabel('Yaxis')
plt.colorbar()  # show color scale
plt.show()

#Pie chart
labels = ['category A','category B','category C','category D']
sizes = [25,35,20,20] #percentage of each category
colors_pie = ['gold','yellowgreen', 'lightcoral','lightskyblue']
explode = (0.1,0.1,0,0)#explode the first slice

plt.pie(labels)
plt.show()