import numpy as np

A = np.array([4,5,1])
B = np.array([2,4,-5,1])

print(np.polyadd(A,B))
print(np.polysub(A,B))
print(np.polymul(A,B))
print(np.polyadd(A,2*B))
