import numpy as np
import time
start=time.time()
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2
print("time for vectorization is ",(time.time()-start))
print(result)  # Output: [2 4 6 8 10]