import numpy as np
import time
arr = np.array([1, 2, 3, 4, 5])
result = []
start=time.time()
for x in arr:
    result.append(x * 2)

print("time for no vectorization is  ",time.time()-start)  # Output: [2, 4, 6, 8, 10]
print(result)
print("hello")
