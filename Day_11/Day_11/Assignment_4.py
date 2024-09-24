import random
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

days = range(1,21)
temps = [round(random.uniform( 15,30),2)for _ in range(20)]
humidity = [random.randint(40, 90) for _ in range(20)]

# Create a pandas DataFrame
weather_data = pd.DataFrame({
    'day': list(days),
    'temp': temps,
    'humidity': humidity
})
print(weather_data)

plt.figure(figsize = (8,6))
sns.lineplot(data=weather_data, x='day', y='temp')
sns.lineplot(data=weather_data, x='day', y='humidity')
plt.title('Temperature lineplot')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid()
plt.show()


plt.figure(figsize = (8,6))
sns.scatterplot(data=weather_data,x='temp',y='humidity' )
plt.title('Temperature vs Humidity Scatterplot')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.show()


plt.figure(figsize = (8,6))
sns.histplot(data = weather_data, x='temp')
plt.title('Temperature Histogram')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(data = weather_data, x='humidity')
plt.title('Humidity Histogram')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.show()