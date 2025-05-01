class Person:
    def __init__(self, name, age):
        self.name = name    # Using self to store the name for the instance
        self.age = age      # Using self to store the age for the instance
        self.greet()

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of Person
person = Person("Alice", 30)



class Temp:

  def __init__(self):
    print('hello')

obj = Temp()


class salman:
   def __init__(self):  # This is basically constructor .
      print('Muhammad salman khan')

obj=salman()