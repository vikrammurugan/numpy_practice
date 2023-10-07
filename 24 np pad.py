import numpy as np
 
 
A = np.ones(shape=(4, 4))
print(np.pad(A, pad_width=1, constant_values=0))