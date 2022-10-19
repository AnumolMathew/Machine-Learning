import numpy as np
print("Anumol Mathew, 007")

#A=np.random.randint(0,8,size=(3,3))
A=np.matrix([[0,2,4],
             [-2,0,3],
             [-4,-3,0]])
print(A)
B=A.transpose()
if A.all() == B.all():
    print("matrix is symmetric ")
else:
    print("not  symmetric")
if np.allclose(-A,B)==True :
    print("matrix is skew symmetric")
else:
    print("not skew symmetric")