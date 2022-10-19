import numpy as np
print("Anumol Mathew, 007")


# define a matrix
A = np.array([[1, 2], [3, 4], [5, 6]])
print("original elements\n",A)
# Singular-value decomposition
U, s, VT = np.linalg.svd(A)
print("U\n",U)
print("s\n",s)
print("VT\n",VT)
# create m x n Sigma matrix
Sigma = np.zeros((A.shape[0], A.shape[1]))
# populate Sigma with n x n diagonal matrix
Sigma[:A.shape[1], :A.shape[1]] = np.diag(s)
# reconstruct matrix
B = U.dot(Sigma.dot(VT))
print(B)