class Student:
    def __init__(self, name):
        self._namename = name  # The underscore (_) indicates a protected variable

    def get_name(self):  # Getter function
        return self._namename
    def set_name(self,value):  # Getter function
        self._namename=value
        return self._namename
    
# Usage
s = Student("Alice")
print(s.get_name())  # Output: Alice
print(s.set_name("salman"))  # Output: salman

