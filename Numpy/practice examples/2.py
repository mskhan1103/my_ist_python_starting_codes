# Create a program that performs matrix addition, subtraction, multiplication, and transpose.
import numpy as np
arr1=np.array([9,2,7,4,5])
arr2=np.array([2,7,3,2,5])
# print("sum of arr1 and arr2 is ",np.sum((arr1,arr2))) # This will return whole sum.
print("sum of arr1 and arr2 is ",arr1+arr2) # while  this will return index wise sum.
print("sub of arr1 and arr2 is ",np.subtract(arr1,arr2))
print("Substraction ",arr1-arr2)
print("Multiplication of arr1 and arr2 is ",np.multiply(arr1,arr2))
print("Multiplication of arr1 and arr2",arr2*arr1)
print("Transpose of array arr1.",arr1.T)
print("Transpose of array arr2.",arr2.T)