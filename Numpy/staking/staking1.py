import numpy as np
arr1=np.arange(10)
arr2=np.arange(10,20)
c=np.hstack((arr1,arr2))
print(c)
#.........this is the horizontal staking of 1d array................
print(np.vstack((arr1,arr2)))
#.........this is the vertical staking of 1d array................



#...............now staking horizontal of 2d array.........
a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
print(np.hstack((a,b)))
print(np.vstack((a,b)))