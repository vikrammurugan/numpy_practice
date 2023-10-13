import numpy as np
 
 
A = np.array([['#summer#time#mood'], ['#sport#time']])
 
print(np.char.strip(np.char.replace(A, '#', ' ')))