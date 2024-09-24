import numpy as np

arr = np.random.randint(50,100,size=(5,5))
print(arr)
# print("\n")
# zero = np.zeros(3)
#
# arr[1:4,1:4]=zero
# print(arr)


zero = np.zeros(3)
arr[1:4,1:4] = zero
print(arr)