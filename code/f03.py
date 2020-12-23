import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing

sns.set()
path = 'C:/Users/User/AppData/Roaming/JetBrains/PyCharmCE2020.2/scratches/'
def cobweb(a0: float, b0: float, a1: float, b1: float, p0: float= 0):
    t = np.array(range(127))
    x_0 = 0
    x0, x1 = [[], []]
    for i in t:
        x0.append(x_0)
        x_1 = (a1 - a0) - (b1 / b0) * x_0
        x1.append(x_1)
        x_0 = x_1
    x0 = np.array(x0)
    x1 = np.array(x1)
    dd = a0 + b0 * x1
    ss = a1 + b1 * x0
    pp = -((a0 - a1) / (b0 - b1))
    time_path = ((p0 - pp) * (b0 / b1) ** -t) + pp
    plt.plot(t, time_path)
    plt.xlabel('periods')
    plt.ylabel('time path')
    plt.savefig(f'{path}/time path-periods.jpg')
    plt.close()
    plt.plot(t, x0)
    plt.xlabel('periods')
    plt.ylabel('price')
    plt.savefig(f'{path}/periods-price.jpg')
    plt.close()
    plt.plot(t, dd + (max(ss) - min(dd)), label='demand')
    plt.plot(t, ss, label='supply')
    plt.xlabel('periods')
    plt.legend()
    plt.savefig(f'{path}/demand and supply-periods.jpg')
    plt.close()
    plt.plot(time_path, dd + (max(ss) - min(dd)), label='demand')
    plt.plot(time_path, ss, label='supply')
    plt.xlabel('time path')
    plt.legend()
    plt.savefig(f'{path}/demand and supply-time path.jpg')
    plt.close()
    cobweb = [[dd[i], ss[i], time_path[i]] for i in range(len(dd))]
    cobweb= pd.DataFrame(data=cobweb, columns=['demand', 'supply', 'price'])
    cobweb.to_csv(f'{path}/cobweb.csv', index= False)

cobweb(a0= 1, b0= -2, a1= 2, b1= 1.5)
def fn02():
    df= pd.read_csv(f'{path}/cobweb.csv')
    x= pd.DataFrame(preprocessing.scale(df), columns=['demand', 'supply', 'price'])
    plt.plot(df['demand'], df['supply'])
    plt.show()

fn02()