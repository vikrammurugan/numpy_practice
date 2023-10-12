import numpy as np


A = np.arange(12, dtype='int').reshape(-1, 4)

A = A[:,::-1]
print(A)