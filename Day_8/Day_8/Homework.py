import numpy as np
from networkx.algorithms.threshold import eigenvalues, eigenvectors

arr = np.random.randint(1,10,size = (3,3))
print(arr)

eigenvalues , eigenvectors = np.linalg.eig(arr)
print(eigenvalues)
print(eigenvectors)

np.savetxt('eigen.txt',np.column_stack((eigenvalues,eigenvectors)),
           delimiter=',',header='Eigenvalues & Eigenvectors',comments='',fmt='%s')