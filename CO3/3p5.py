import matplotlib.pyplot as plt
import numpy as np

print("Anumol Mathew, 007")

plt.xlabel('mode of transport')
plt.ylabel('frequency')
plt.title("transportation data",loc='left')

x=np.array(['walking','cycling','car','bus','train'])
y=np.array([29,15,35,18,3])
plt.plot(x,y,color='green',linewidth=1)
plt.show()