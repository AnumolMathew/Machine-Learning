import matplotlib.pyplot as plt
import numpy as np

print("Anumol Mathew, 007")


x=np.array(['Mon','Tues','Wed','Thurs','Fri'])
y=np.array([300,450,150,400,650])

plt.subplot(1,2,1)
plt.plot(x,y,color='c',linestyle='dotted',marker='h',mfc='m',mec='k')
plt.xlabel('days of weeks')
plt.ylabel('sales of drinks')
plt.title("sales data1",loc='right')
plt.grid(color='blue',linestyle='dotted')



x=np.array(['Mon','Tues','Wed','Thurs','Fri'])
y=np.array([400,500,350,300,500])

plt.subplot(1,2,2)
plt.plot(x,y,color='y',linestyle='dashed',marker='d',mfc='g',mec='r')
plt.xlabel('days of weeks')
plt.ylabel('sales of food')
plt.title("sales data2",loc='center')

plt.grid(color='pink',linestyle='dotted')
plt.show()
