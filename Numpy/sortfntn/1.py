import numpy as np
a=np.random.randint(1,10,10).reshape(2,5)
print(a)
print(np.sort(a,axis=0))
print(np.append(a,(np.ones(5)),axis=0)) 