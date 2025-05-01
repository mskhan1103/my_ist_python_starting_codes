# fntn that will check if a given is even or odd.

def is_even(num):
    if type(num)==int:
      if num%2==0:
       return "even"

      else:
        return "odd"

    else:
       print("only integer values is allowed.")
#is_even("hello")
for i in range(1,11):
   x=is_even(i)
   print(x)


