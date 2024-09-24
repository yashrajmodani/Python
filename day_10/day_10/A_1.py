import numpy as np

list1 = [0, 1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
list3 = [10, 11, 12, 13, 14]
list4 = [15, 16, 17, 18, 19]

arr1 = np.array([list1,list2])
print(arr1)

arr2 = np.array([list3,list4])
print(arr2)
print("----------ADDITION----------")
arr3 = arr1 + arr2
# arr3 = np.add(arr1,arr2)
print(arr3)

print("----------SUBTRACT-------------")
arr4 = np.subtract(arr2,arr1)
print(arr4)
print("---------MULTIPLY--------------")
arr5 = np.multiply(arr1,arr2)
print(arr5)
print("---------EXPONENTIAL---------------")
arr6 = np.exp(arr1)
print(arr6)