import numpy as np

print(np.arange(10,100,1).reshape(9,10))

 
print(np.arange(10, 100).reshape(9, 10))
 
print(np.arange(10, 100).reshape(9, -1))
print(np.arange(10, 100).reshape(-1, 10)) 