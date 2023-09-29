import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])


for i,j in zip(list('ABCD'),[A,B,C]):
    print(f"{i}: {np.all(j,axis=1)}")