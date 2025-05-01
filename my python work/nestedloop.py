# Code here
for i in range(0,3):
  print(" "*(3-i-1) + "* "*(2*i+1))


for i in range(1,6):
  for j in range(i,0,-1):
    print(j,end=" ")
  print()


n=int(input("input any no ......"))
res=0
for i in range(1,n+1):
  res=res+n**2/n

print(res)


result = []  

for num in range(1000, 3001):  
    num_str = str(num)  # Convert number to string for digit checking
    
    if all(int(digit) % 2 == 0 for digit in num_str):  
        result.append(num)  

print(" ".join(map(str, result)))  



import math  

x, y = 0, 0  # Starting position

while True:  
    move = input("Enter movement (or '!' to stop): ").strip()  
    
    if move == "!":  
        break  
    
    direction, steps = move.split()  # Split input into direction and steps
    steps = int(steps)  # Convert steps to integer

    if direction == "UP":  
        y += steps  
    elif direction == "DOWN":  
        y -= steps  
    elif direction == "LEFT":  
        x -= steps  
    elif direction == "RIGHT":  
        x += steps  

# Calculate Euclidean distance from (0,0)
distance = math.sqrt(x**2 + y**2)  

print(round(distance))  # Print nearest integer
