import pandas as pd
import numpy as np

n = np.arange(10)
a = pd.Series([-1, 1, 3, 5, 7])
a * 10

a.index = ['a', 'b', 'c', 'd', 'e']
print(n)
print(a)

slownik = {'roślina': ['lilak', 'thuja', 'tulipan'], 'Ilość': [6, 99, 20], 'xxx': ['a', 'b', 'c']}

ogrod = pd.DataFrame(slownik, columns=['roślina', 'xxx', 'Ilość', 'miejsce'])
ogrod.index = ['grządka 1', 'grządka 2', 'grządka 3']
print(ogrod)

print(ogrod.describe())
