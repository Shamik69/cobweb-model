import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
a0, b0, a1, b1, p0= [1, -2, 2, 1.9, 0]
t= np.array(range(500))
x_0= 0
x0, x1= [[], []]
for i in t:
  x0.append(x_0)
  x_1= (a1- a0)- (b1/b0)*x_0
  x1.append(x_1)
  x_0= x_1
x0= np.array(x0)
x1= np.array(x1)
dd= a0+ b0*x1
ss= a1 + b1*x0
pp= -((a0-a1)/(b0-b1))
time_path= ((p0- pp)*(b0/b1)**-t)+ pp
plt.plot(t, time_path)
plt.xlabel('periods')
plt.ylabel('time path')
plt.show()
plt.plot(t, x0)
plt.xlabel('periods')
plt.ylabel('price')
plt.show()
plt.plot(t, dd+(max(ss)-min(dd)), label= 'demand')
plt.plot(t, ss, label= 'supply')
plt.xlabel('periods')
plt.legend()
plt.show()
plt.plot(time_path, dd+(max(ss)-min(dd)), label= 'demand')
plt.plot(time_path, ss, label= 'supply')
plt.xlabel('time path')
plt.legend()
plt.show()