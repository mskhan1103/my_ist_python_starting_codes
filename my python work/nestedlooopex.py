# Code here
for i in range(5,0,-1):
  for j in range(i,0,-1):
   print(j,end=" ")
  print()


for i in range(5, 0, -1):  # Outer loop for rows, starting from 5 down to 1
    for j in range(i, 0, -1):  # Inner loop for columns, printing numbers from i down to 1
        print(j, end="  ")  # Print the number with a space
    print()  # Move to the next line


for i in range(1,6):
   for j in range(1,i):
      print(" * ", end=" ")
   print()
   for i in range(6,1,-1):
      for j in range(i,1,-1):
         print(" * ",end=" ")
      print()

# Code here
for i in range(3,0):
  print(" "*(3-i-1) + "* "*(2*i+1))