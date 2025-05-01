
import time
#.....for python list it takes 3.02 seconds to add 1crore+1crore elemnts of two lists together
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
start=time.time()
for i in range(len(a)):
    c=a[i]+b[i]
print("time passed here is ",time.time()-start)
#...........for numpy array it takes  about 54 times less time to add a above elemnts.
import numpy as np
a=np.arange(10000000)
b=np.arange(10000000)
start=time.time()
c=a+b
print("time passed here is ",time.time()-start)
