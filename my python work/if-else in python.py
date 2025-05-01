#...if else are used  in programming when there is branching occur means we have many decisions based on single idea...
#...example...
#email=input("enter your email ist ....")
#password=input("enter your password .......")

#if email=="salman@gmail.com" and password=="234":
  #  print("welcm")
#elif email=="salman@gmail.com" and password!="234":
 #   input("your password is incorect enter again ..")
    
#else :
 #   print("incorrect")


#.....................programe that will find min value in three input integers .............
#a=int(input("enter ist num .."))
#b=int(input("enter 2 num ..")) 
#c=int(input("enter 3 num .."))
#if a<b and a<c:
#    print("a is min ie ",a)
#elif b<c:
#   print("min is ",b)
#else:
 #   print("min is ",c)


#/////////////..............simple calculator................///////////////
#num1=int(input("enter num 1 "))
#num2=int(input("enter num 2 "))
#op=input("enter operator .......")

#if op=="+":
 #   print(num1+num2)
#elif op=="-":
 #   print(num1-num2)
#elif op=="*": 
# print(num1*num2)
#else :
#    print(num1/num2)



#//////////////////..........table formation through while loop ...........//////////////////

#num=int(input("enter a no to make table of ...."))
#i=1
#while i<11:
#    print(num, " * " ,i ," = ", num*i)
 #   i +=1
   

#.....programe that will enter 3 no int value from the user and will add all the three value together
#num=int(input("enter a threee digit value ............."))

#.....567.....
#a = num%10

#num=num//10

#.............57.......
#b=num%10

#num//10

#.............5........
#c=num%10
#print(a+b+c)


#////////////////////////////////////....elid.......................
#a=10

#b=100

#if a>b:
 #   print(b)
#elif a==b:
 #   print(2)
#else:
 #   print(9)

#a = 2
#b = 330
#print("A") if a > b else print("B")

#/////////..............while loop............
#i = 1
#while i < 6:
 # print(i)
 # i +=1

#............break statement ..........
#i = 1
#while i < 6:
 # print(i)
 # if i == 1:
 #   break
 # i += 1

for x in range(2, 102, 3):
  print(x)