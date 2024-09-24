import numpy as np

arr = np.arange(1,17)
print(arr)

x = np.sqrt(arr)
print(x)

np.savetxt("Square_root_results.csv",arr,delimiter=',')
np.savetxt("Square_root_cal.csv",x,delimiter=',')