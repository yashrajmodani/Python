import numpy as np

A = np.random.randint(1,9,size=(4,2))
B = np.random.randint(1,9,size=(2,3))

mul = np.matmul(A,B)
res = mul.T
print(A)
print(B)
print(mul)
print(res)