import numpy as np
samples = np.random.normal(size=(4,4))
print(samples)

"""
1. np.random.rand()
Generates random floats between 0 and 1 from a uniform distribution.

Returns a scalar or array depending on arguments.
"""
print(np.random.rand())         # Single float e.g. 0.753
print(np.random.rand(2, 3))    # 2x3 array of random floats

"""
2. np.random.randint(low, high, size)
Generates random integers between low (inclusive) and high (exclusive).

size defines shape of the output array.

python
Copy
Edit
"""
np.random.randint(1, 10)          # Single integer
np.random.randint(1, 10, size=5)  # 1D array with 5 random ints

"""
3. np.random.randn()
Generates samples from a standard normal distribution (mean = 0, std = 1).
"""
np.random.randn(3)        # 1D array with 3 samples
np.random.randn(2, 2)     # 2x2 array of normally-distributed values


"""
4. np.random.choice()
Randomly pick elements from a given 1D array.

python
Copy
Edit
"""
arr = [10, 20, 30, 40]
np.random.choice(arr, size=2)  # Randomly picks 2 values
