import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                     [[7, 8, 9], [10, 11, 12]],
                     [[13, 14, 15], [16, 17, 18]]])

#
# print(array_1d.ndim, array_1d.shape)
# print(array_2d.ndim, array_2d.shape)
# print(array_3d.ndim, array_3d.shape)
# # #
def describe_array(arr):
    print(f"ndim = {arr.ndim} ")
    print(f'shape: {arr.shape}')
    print(f'size: {arr.size}')
    print(f'dtype: {arr.dtype}\n')


describe_array(array_1d)
describe_array(array_2d)
describe_array(array_3d)

