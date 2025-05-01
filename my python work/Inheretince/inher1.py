# Parent class
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an object of Dog
dog = Dog()
dog.make_sound()  # Inherited from Animal class
dog.bark()        # Defined in Dog class
