import numpy as np
print("Anumol Mathew, 007")

x=np.matrix([[2,3],
             [3,4]])
print(x)
print("cube using multiply fn :\n",np.multiply(x,np.multiply(x,x)))
print("cube using power fn :\n",np.power(x,3))
print("cube using '**'\n",x**3)
print("cube using '*'\n",x*x*x)
print('identity matrix is:\n',np.identity(2,dtype=int))
print("Display each element of the matrix to different powers.\n",np.power(x,[[1,2],[3,4]]))
print("matrix multiplication\n",x@x)
y=np.matrix([[3,7],
              [8,9]])
print("x^2+2y\n",(x**2)+(2*y))
