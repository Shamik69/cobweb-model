import numpy as np
import matplotlib.pyplot as plt

n= 100
a0= -588282
a1= 2
ratio_exp= 0.95
y0= []
y1= []
y2= []
x= []
err= ratio_exp-abs(a0/a1)
print(err)
for i in range(n):
    ratio= abs(a1/a0)
    a0+=err
    y0+=[a0]
    err= ratio_exp-abs(a1/a0)
    y1+=[a1]
    y2+=[ratio]
    x+=[i]
    if ratio< ratio_exp:
        print(i)
        break
print(f'{y0}\n{y1}\n{y2}')
y0= np.array(y0)-np.array(y0).mean()
y1= np.array(y1)-np.array(y1).mean()
y0= np.array(y2)-np.array(y2).mean()
y0= np.array(y0)-np.array(y0).mean()

plt.plot(x, y0, label= 'a0')
plt.plot(x, y1, label= 'a1')
plt.plot(x, y2, label= 'ratio')
plt.legend()
plt.show()