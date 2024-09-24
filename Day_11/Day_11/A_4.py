import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
y1=np.array([1,3,4,7,9,12,15,18,19,22])
y2=np.array([2,5,7,10,12,13,16,18,21,23])
fig, axs = plt.subplots(2,2,figsize =(12,10))#2X2 GRID SIXE OF THE PLOT

#Line chart
axs[0,0].plot(x,y1,label = 'Dataset1',color = 'blue', marker = 'o',linestyle = '--')
axs[0,0].plot(x,y2,label = 'Dataset2',color = 'red', marker = 's',linestyle = '-')
axs[0,0].set_title('Line plot example')
axs[0,0].set_xlabel('x-axis')
axs[0,0].set_ylabel('y-axis')

axs[0,0].legend()
axs[0,0].grid(True)


#Bar Chart
categories = ['category A','category B','category C','category D']
values = [4,7,1,8]

axs[0,1].bar(categories,values,color = 'orange')
axs[0,1].set_title('Bar Chart example')
axs[0,1].set_xlabel('categories')
axs[0,1].set_ylabel('values')

#Scatter Plot

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

axs[1,0].scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
axs[1,0].set_title('Scatter plot example')
axs[1,0].set_xlabel('X axis')
axs[1,0].set_ylabel('Yaxis')
# plt.legend(loc = "upper_left")
plt.show()


