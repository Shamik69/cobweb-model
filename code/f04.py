import pandas as pd
import matplotlib.pyplot as plt

path = 'C:/Users/User/PycharmProjects/cobweb-model'

df = pd.read_csv(f'{path}/data/cobweb.csv')

plt.scatter(df.quantity, df.price)
plt.show()
