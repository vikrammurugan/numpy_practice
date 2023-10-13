import numpy as np


A = np.array(['001', '002', '003'], dtype=np.str_)
B = np.array(['XC', 'YC', 'ZC'], dtype=np.str_)

print(np.char.add(A,B))