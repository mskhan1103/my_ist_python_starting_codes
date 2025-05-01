""""""
#FizzBuzz

#Print numbers from 1 to 100.
#If a number is divisible by 3, print "Fizz."
#If it's divisible by 5, print "Buzz."
#If it's divisible by both, print "FizzBuzz."

""""""
#............start .......................#

def Fizzbuzz(num):
  for i in range(0,100):
     if num[i]%3==0 and num[i]%5==0:
        print("Fizzbuzz")
     elif num[i]%3==0:
        print("Fizz")
     elif num[i]%5==0:
        print("Buzz")
    
        
     else:
        print(num[i])

L=[i for i in range(0,100)]
Fizzbuzz(L)





# Palindrome Checker

#Ask the user to enter a string.
#Check if the string is the same when reversed.
#Example: "racecar" is a palindrome, but "hello" is not.


def pallindrome(s):
   last=True
   for i in s:
      if s[0]==s[-1]:
         last=False
   if not last:
         print("pallendrome")
   else:
      print("Not a pallendrome.")

   

s=input("Enter a string to check if it is pallendrome or ")
pallindrome(s)



# Prime Number Checker

#Ask the user for a number.
#Check if the number is prime or not.

def prime(no):
   for i in range():
    pass