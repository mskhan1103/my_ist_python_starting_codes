def is_even(num):
    """
    This fntn will take only one argument and will if the given fntn is even or odd.
    """
    if type(num)==int:
     if num%2==0:
        return "Even"
     else:
        return ("odd")
    else:
       return "Only integer values can be passed."


# print(is_even("hello"))
for i in range(1,11):
   x=is_even(i)
   print(x)


# Parameter types .
# 1 default parameter.
def default(a=1,b=3):
   print(a*b)

default(2)

# Positional Argument

def position(a,b):
   print(a**b)


position(2,2)



# Keyword Argument
position(b=2,a=7)



# *arg in python. (Are used to send many arguments without being worring about it.)

def multiply(*num):
  x1 = 1
  for i in num:
   
   x1=x1*i
   print(x1)


multiply(2,3,4,32,32,3,22,22,2)

# **kwargs arguments.
# it allow us to send many no of key word arguments.
def kwrg(**capitals):
   for i,j in capitals.items():
      print(i,"->",j)

kwrg(india="delhi",pakistan="islamabad",nepal="katmandhu")



# nested function ......
def f():
  def g(): # this is nested one.
    print('inside function g')
 # f() this is will cause max recursion.
  g()
  print('inside function f')
f()
