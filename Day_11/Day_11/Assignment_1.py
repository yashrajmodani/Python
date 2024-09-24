import numpy as np

from scipy.linalg import inv

matrix = np.array([[4, 7], [2, 6]])
print(matrix)
matrix_inv = inv(matrix)
print(matrix_inv)
