# local and global

# global var
a = 2

def temp():
  # local var
  b = 3
  print(b)
   # since a is global var thats why we can access it from inside fntn.
  
  a=5+2
  print(a)
  #a=a+3 # here we are trying to update value of a which is not allowed we can only use it not updates it.

temp()
print(a)
#print(b) # error bcz we are trying to access local var of a fntn which is not allowed.