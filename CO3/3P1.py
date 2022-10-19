import matplotlib.pyplot as plt
import numpy as np

print("Anumol Mathew, 007")

plt.xlabel('year')
plt.ylabel('value')
plt.title("value depreciation ",loc='left')

x=np.array([2001,2002,2003,2004,2005 ,2006 ,2007])
y=np.array([24000,22500,19700,17000,14500,10000,5800])

plt.plot(x,y,color='r',linestyle='dashed',marker='*',mfc='g',ms=20)
plt.show()
