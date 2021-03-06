import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing

sns.set()
path = 'C:/Users/User/PycharmProjects/cobweb-model'


def cobweb(a0: float, b0: float, a1: float, b1: float, p0: float = 0):
    t = np.array(range(500))
    x_0 = p0
    x0, x1 = [[], []]
    for i in t:
        x0.append(x_0)
        x_1 = ((a1 - a0) + (b1 * x_0))/b0
        x1.append(x_1)
        x_0 = x_1
        if round(x1[i], 2) - round(x0[i], 2)==0:
            t= np.array(range(len(x0)))
            break
    x0 = np.array(x0)
    x1 = np.array(x1)
    dd = a0 + b0 * x1
    ss = a1 + b1 * x0
    pp = -((a0 - a1) / (b0 - b1))
    time_path = ((p0 - pp) * (b0 / b1) ** t) + pp
    plt.plot(t, time_path)
    plt.xlabel('periods')
    plt.ylabel('time path')
    plt.savefig(f'{path}/figs/time path-periods.jpg')
    plt.close()
    plt.plot(t, x0)
    plt.xlabel('periods')
    plt.ylabel('price')
    plt.savefig(f'{path}/figs/periods-price.jpg')
    plt.close()
    plt.plot(time_path, x0)
    plt.xlabel('time path')
    plt.ylabel('price')
    plt.savefig(f'{path}/figs/time path-price.jpg')
    plt.close()
    plt.plot(t, dd)
    plt.xlabel('periods')
    plt.ylabel('quantity')
    plt.legend()
    plt.savefig(f'{path}/figs/quantity-periods.jpg')
    plt.close()
    plt.plot(time_path, dd)
    plt.xlabel('time path')
    plt.ylabel('quantity')
    plt.legend()
    plt.savefig(f'{path}/figs/quantity-time path.jpg')
    plt.close()
    plt.plot(x0, dd)
    plt.xlabel('price')
    plt.ylabel('quantity')
    plt.legend()
    plt.savefig(f'{path}/figs/quantity-price.jpg')
    cobweb = [[t[i], round(dd[i], 2), round(time_path[i], 2), round(x1[i], 2)] for i in range(len(dd))]
    cobweb = pd.DataFrame(data=cobweb, columns=['periods', 'quantity', 'time path', 'price'])
    cobweb.to_csv(f'{path}/data/cobweb.csv', index=False)


cobweb(a0=1, b0=-2, a1=-0.5, b1=1.95)


def fn02():
    df = pd.read_csv(f'{path}/data/cobweb.csv')
    x = pd.DataFrame(preprocessing.scale(df), columns=['periods', 'quantity', 'time path', 'price'])


fn02()
