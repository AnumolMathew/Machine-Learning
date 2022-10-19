import numpy as np
print("Anumol Mathew, 007")

a = np.array([[1, 2,4],
              [3, 5,6],
              [7,8,9]])
b = np.array([1, 2, 7])
x = np.linalg.solve(a, b)
print("vector x=\n",x)
print("\n",np.allclose(np.dot(a, x), b))
