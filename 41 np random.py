import numpy as np


np.random.seed(42)

A=np.random.randint(low=0,high=256,size=(200,300,3),dtype=np.uint8)

print(A)