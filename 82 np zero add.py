import numpy as np

A = np.array(['1', '2', '3'], dtype=np.str_)

print(np.char.zfill(A,width=4))