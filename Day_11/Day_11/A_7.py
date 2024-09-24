import plotly.graph_objects as go
import numpy as np

# Generate_sunthetic_data

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = np.random.randint(50, 500, size=12)

# Line Plot
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(x=months, y=sales, mode='lines+markers', name='Sales'))
line_fig.update_layout(title="Monthly Sales Data", xaxis_title="Months", yaxis_title="Sale")
line_fig.write_image('line_plot.png')

# Bar Chart
bar_fig = go.Figure()
bar_fig.add_trace(go.Bar(x=months, y=sales, name="Sales"))
bar_fig.update_layout(title='Monthly Sales Data Bar Chart', xaxis_title='Months', yaxis_title="Sale")
bar_fig.write_image('bar chart.png')

# Pie Chart

total_sales = np.sum(sales)
pie_fig = go.Figure()
pie_fig.add_trace(go.Pie(labels=months, values=sales, name='Sales Distribution'))
pie_fig.write_image('pie_chart.png')
print("PLots generated and saved")
