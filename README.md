
# Python Code Examples

This repository is a collection of **Python code examples and scripts** across various topics. It serves as a reference for learning Python, practicing coding, and experimenting with different programming concepts.

---

## Repository Structure



python-codes/
├── basics/ # Basic Python concepts: variables, loops, conditionals
├── data-structures/ # Lists, dictionaries, sets, tuples, etc.
├── functions/ # Functions, recursion, lambda, etc.
├── file-io/ # Reading/writing files, CSV, JSON
├── oops/ # Object-Oriented Programming examples
├── algorithms/ # Sorting, searching, and other algorithms
├── utilities/ # Helper scripts and useful utilities
└── README.md # This file


---

## Topics Covered

### 1. Basics
- Variables, data types, and operators
- Loops (`for`, `while`)
- Conditionals (`if`, `elif`, `else`)
- Example:
```python
# Check if a number is even or odd
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

2. Data Structures

Lists, Tuples, Dictionaries, Sets

Example:

# Count frequency of elements in a list
lst = [1,2,2,3,3,3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)

3. Functions

Defining and calling functions

Recursion and lambda functions

Example:

# Factorial using recursion
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
print(factorial(5))

4. File I/O

Reading/writing text files

Working with CSV and JSON

Example:

# Write a list to a file
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

5. Object-Oriented Programming

Classes, objects, inheritance, encapsulation

Example:

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, {self.name}!")
p = Person("Salman")
p.greet()

6. Algorithms

Sorting, Searching, Recursion

Example:

# Bubble sort
arr = [5,3,1,4,2]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

How to Use

Clone the repository:

git clone https://github.com/msalmankhan03/Python-Codes.git


Navigate to the folder of interest:

cd python-codes/basics


Run any Python script:

python example.py

Contributing

Add new examples under the appropriate topic folder.

Include a short comment or README snippet explaining the code.

License

MIT License


