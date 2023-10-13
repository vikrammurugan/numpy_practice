import numpy as np
 
 
A = np.arange('2021-01', '2022-01', dtype='datetime64[M]')
A = A.reshape(-1, 3)
print(A)