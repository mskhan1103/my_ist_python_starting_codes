
#..............minimum..........................

#mylist=[24,5,43,34,55,44]

#min=mylist[0]

#for  num in  mylist:
 #   if min  >  num :
  #      min=num

#print(min)

#...................max.........................
#maxlist=[24,5,43,34,55,44]

#max=maxlist[0]

#for num in maxlist:
   # if max < num :
     #   max=num


#print(max)


#Write a program that prints the numbers from 1 to 100. But for multiples of 3,
#  print "Fizz" instead of the number, and for multiples of 5, 
# print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

n=1
while n<=100:
  
    if n%3==0:
        print("fizz")
    elif n%5==0:
       print("Buzz")
    else :
     print(n)
    n +=1
    
