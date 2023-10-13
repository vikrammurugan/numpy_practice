import numpy as np

now=np.datetime64('now')

print(now.astype('datetime64[D]').astype(str))


import numpy as np
 
 
print(np.datetime64('today'))