print("Anumol Mathew 07")

import numpy as np

arr = np.array([
            [1+4j,2+5j,3+6j],
            [4+6j,9+1j,5+2j],
               ],
            dtype=complex)
print(arr)
print("\ndimension of given array is :",arr.ndim)
print("\nnumber of rows and columns of given array is :",arr.shape)

newarr = arr.reshape(3,2)
print("\nnew array is :",newarr)