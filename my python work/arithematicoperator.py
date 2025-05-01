# We have six arithamatic operator in python

#................prorame that will take three digit input from the user at once and and will add all the three values..
   #..........234.........
number=int(input("enter three digit value....")) # explicit type conversion.
#..............a = 4........
a=(number%10)
number=(number//10) # number = 234//10 = 23.0
#............b=3........
b=number%10
number=number//10 # number=23//10=2
#..............c=2..........
c=number%10
print(c+a+b)