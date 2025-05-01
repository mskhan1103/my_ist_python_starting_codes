import numpy as np
"""
Simulate rolling a dice 1000 times using NumPy and analyze the frequency of each face.

"""

dice_rolls=np.random.randint(1,7,size=1000)
face_counts = np.bincount(dice_rolls)[1:] # since bicount start counting indexing from 0 that why we have used [1:]
print(face_counts)
