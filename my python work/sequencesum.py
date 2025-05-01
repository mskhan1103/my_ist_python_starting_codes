num=int(input("Enter any no .................")) #5
result=0
fact=1
for i in range(1,num+1):
    fact=fact*i
    result=result+i/fact


print(result)


#..........right angle triangle through esterick.......

for i in range(1,6):
    for j in range(1,i+1):
        print( " * ",end=" ")
        
    print()


#........another example ............
num=int(input("eneter any no ............."))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


