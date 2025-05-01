class Student:
    school_name = "ABC High School"  # Static (class) variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Creating objects
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

# Accessing static variable
print(s1.school_name)  # Output: ABC High School
print(s2.school_name)  # Output: ABC High School

# Changing static variable
Student.school_name = "XYZ Academy"

print(s1.school_name)  # Output: XYZ Academy
print(s2.school_name)  # Output: XYZ Academy
