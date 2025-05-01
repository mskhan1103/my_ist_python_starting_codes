import numpy as np

data = np.random.randn(1000)  # 1000 values from standard normal distribution
print(data[:100])               # Print first 5 values
"""
What It Does:
It generates 1000 random numbers from a standard normal distribution, i.e., a bell-shaped curve with:

Mean (μ) = 0

Standard Deviation (σ) = 1

What Kind of Numbers Are These?
Most of these 1000 numbers will be close to 0 (like between -1 and +1).

Some values will be farther from 0 (like -2.5 or +2.1), but such values are less frequent.

Very extreme values (like -4 or +4) are rare.

"""