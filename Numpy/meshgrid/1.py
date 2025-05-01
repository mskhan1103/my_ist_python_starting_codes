import numpy as np
x=np.array([1,2,3])
y=np.array([4,5])
x,y=np.meshgrid(x,y)
print(x)
print(y)
# example 2
x = np.array([0, 1])
y = np.array([10, 20, 30])

X, Y = np.meshgrid(x, y)

print("X =\n", X)
print("Y =\n", Y)
