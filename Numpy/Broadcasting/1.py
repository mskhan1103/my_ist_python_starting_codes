import numpy as np
arr1=np.arange(20).reshape(4,5)
arr2=np.arange(20).reshape(4,5)
print(arr1+arr2)
#  operands can be broadcasted together b/c of same dimension.

arr3=np.arange(5).reshape(5) #(1,5)->(4,5)
arr4=np.arange(20).reshape(4,5)
print("can  be broacasted .",arr3+arr4)


#ValueError: operands could not be broadcast together with shapes (5,1) (4,5) 
a=np.arange(5).reshape(5,1) #(5,5)->(4,5)
b=np.arange(20).reshape(4,5)
print(a+b)


"""
arr5=np.arange(25).reshape(5,5)
arr6=np.arange(20).reshape(4,5)
print(arr1+arr2)
#  operands cannot be broadcasted together b/c of different dimension.
"""
