
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
my_function("Pakistan")



def my_function(food):
  for x in food:
    print(x)

fruits = [1,0]

my_function(fruits)
   

def my_function(x):
 return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



def salman():
  return "salman function ............"


print(salman())



#........................lambda function ...........
y=lambda a: print(a)

y(60000000000)


def args(username, greeting):
    print("Hello, {}, From My Function!, I wish you {}".format(username, greeting))

args("salman ","best of luck .")

a = 10
b = 5

print(f"The sum of {a} and {b} is {a + b}.")


def std(*num1):
    total = sum(num1)
    print(f"sum of  {total}")

std(12, 34, 67)

a=10
b=2000
print(f"sum of {a} and {b} is {a+b}")


name="salman"
age=20
khan="jjjjjjj"

print("%s is   %a %s old"% (name,age,khan))