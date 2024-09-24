# creating a date range
import pandas as pd
import numpy as np

dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
print(dates.dtype, dates, '\n')
print('-----------------------------------------------')
# creating a time series with random data
data = np.random.randn(10)
time_series = pd.Series(data, index=dates)
print(time_series)
print('-----------------------------------------------')
# accessing data for a specific date
print("Time series for - '2024-01-05' ", time_series['2024-01-05'])
print('-----------------------------------------------')
# Accessing data within a date range
print('Time series for range : \n', time_series['2024-01-03':'2024-01-06'])
print('-----------------------------------------------')
print('With boolean Indexing : \n', time_series[time_series > 0])
print('-----------------------------------------------')

hourly_dates = pd.date_range(start='2024-01-01', periods=24, freq='h')
hourly_data = np.random.randn(24)
hourly_series = pd.Series(hourly_data, index=hourly_dates)
print('Complete hourly series \n', hourly_series)
print('-----------------------------------------------')

print('Hourly series:', hourly_series['2024-01-01 15:00'])
print('-----------------------------------------------')
print("Data with multiple condition: \n", time_series['2024-01-01':'2024-01-10'][time_series > 0])
print('-----------------------------------------------')
print(time_series.loc['2024-01-05'])
print('-----------------------------------------------')
print(time_series.loc['2024-01-03':'2024-01-06'])
print('-----------------------------------------------')
print(time_series.iloc[0])
print('-----------------------------------------------')
print(time_series.iloc[2:6])
print('-----------------------------------------------')
print(time_series.iloc[[0, 3, 7]])
print('-----------------------------------------------')
time_series['2024-01-04'] = np.nan
print(time_series)

print('-----------------------------------------------')
filled_series = time_series.ffill()
print(filled_series)
print('-----------------------------------------------')

weekly_series = time_series.resample('W').mean()
print(weekly_series)
print('-----------------------------------------------')
filled_backward = time_series.bfill()
print(filled_backward)
print('-----------------------------------------------')

interpolated = time_series.interpolate()
print(interpolated)
