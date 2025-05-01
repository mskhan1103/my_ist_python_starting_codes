import numpy as np
arr=np.arange(20).reshape(5,4)
print(arr)
# fetch 1st row
print(arr[0:1,:])
# fetch 9,10 and 13,14
print(arr[2:4,1:3])
# fetch 5
print(arr[1,1])
# fetch 0,3 and 16,19
print(arr[::4,::3])
# fetch 1st and 2nd coloumn
print(arr[:,1:3])