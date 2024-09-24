import numpy as np

int_arr = np.array([[1, 2, 3], [4, 5, 6]])
float_arr = np.array([[1.43, 2.52, 3.76], [4.45, 5.34, 6.32]])
bool_arr = np.array([[True, False, False], [True, False, True]])

print(f"item size of int array: {int_arr.itemsize}")
print(f"item size of float array: {float_arr.itemsize}")
print(f"item size of boolean array: {bool_arr.itemsize}\n")

print(f"nbyte of int array: {int_arr.nbytes}")
print(f"nbyte of float array: {float_arr.nbytes}")
print(f"nbyte of boolean array: {bool_arr.nbytes}")
