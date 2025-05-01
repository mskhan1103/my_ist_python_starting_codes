# A simple list
"""numbers = [5, 10, 15, 20, 25]

# Create a Boolean mask: select numbers greater than 15
mask = [n > 15 for n in numbers] 
print(mask)
# Output: [False, False, False, True, True]

# Use the mask to filter numbers
filtered = [n for n, m in zip(numbers, mask) if m]
print(filtered)
# Output: [20, 25]

# This was example without numpy array.


#,........................with numpy array..............................,#
import numpy as np

# Create a NumPy array
arr = np.array([5, 10, 15, 20, 25])

# Create a Boolean mask: numbers greater than 15
mask = arr > 15
print(mask)
# Output: [False False False  True  True]

# Apply the mask
filtered = arr[mask]
print(filtered)
# Output: [20 25]



#......................other example of masking in numpy

arr=np.arange(10).reshape(2,5)
print(arr)
# now select no that are even.
print(arr%2==0)
print(arr[arr%2==0])

# now select no that are even and > than 5.
print((arr%2==0) & (arr>5))
print(arr[(arr%2==0) & (arr>5)])


# Example 4: Replace Elements Less Than 5 With 0
arr = np.array([2, 5, 7, 3, 10])
arr[arr < 5] = 0
print(arr)   # [ 0  5  7  0 10]


#Example 5: Select Elements That Are Odd and Greater Than 5
arr_odd = np.array([2, 5, 7, 3, 9,10])
print((arr_odd%2==1) & (arr_odd>5))
print(arr_odd[(arr_odd%2==1) & (arr_odd>5)])
"""

# Example 6: Mask in 2D Arrays
import numpy as np
arr2d=np.arange(20).reshape(5,4)
print(arr2d)
print(arr2d%2==0)
print(arr2d[arr2d%2==0].reshape(5,2)) # reshaping the masked array into another (5,2) array.


# Example 7: Replace All Values > 10 With 10
arr = np.array([8, 10, 12, 15])
arr[arr > 10] = 10
print(arr)   # [ 8 10 10 10]


# Example 8: Set Negative Numbers to Zero
arr1=np.array([-1,2,3,-4,-5])
arr1[arr1<0]=0
print(arr1)