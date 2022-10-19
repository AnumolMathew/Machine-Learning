import numpy as np
print("Anumol Mathew, 007")

mat=np.random.randint(8,size=(3,3))
print(mat)
print('inverse is:\n',np.linalg.inv(mat))
print('rank of matrix is:\n',np.linalg.matrix_rank(mat))
print("determinant of matrix is :\n",np.linalg.det(mat))
print("transform matrix into 1D array\n",mat.flatten(order='c'))
print("transform matrix into 1D array\n",mat.flatten(order='f'))
v1, v2 =np.linalg.eig(mat)
print("eigen values are :\n",v1)
print("eigen vectors are :\n",v2)