

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)




import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)




numbers = [10, 20, 30, 40]

print("List (array):", numbers)
print("First element:", numbers[0])

# Add a new number
numbers.append(50)
print("After append:", numbers)





# Function without parameters
def greet():
    print("Hello!")

# Function with parameters
def add(a, b):
    return a + b

# Calling the functions
greet()
result = add(5, 3)
print("Sum:", result)





# List: Ordered, changeable
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("First fruit:", fruits[0])

# Tuple: Ordered, unchangeable
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("Second color:", colors[1])

# Set: Unordered, no duplicates
numbers = {1, 2, 3, 2}
print("Set:", numbers)

# Dictionary: Key-value pairs
person = {"name": "Alice", "age": 25}
print("Dictionary:", person)
print("Name:", person["name"])






a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Comparison Operators
print("Equal:", a == b)
print("Not equal:", a != b)
print("Greater than:", a > b)

# Logical Operators
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)





name = "John"
print("Name:", name)

# String operations
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("First letter:", name[0])
print("Length:", len(name))
print("Greeting:", "Hello " + name)






name = "Alice"
greeting = "Hello"
message = greeting + ", " + name + "!"  # String concatenation

print(message)
print("Length of name:", len(name))     # String length
print("Uppercase:", name.upper())       # Uppercase
print("First letter:", name[0])         # Accessing character








age = 20              # int
height = 5.9          # float
name = "John"         # str
grade = 'A'           # str (single character)
passed = True         # bool

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Grade:", grade)
print("Passed:", passed)





a = 10        # Integer
b = 3.5       # Float
c = a + b     # Addition
d = a * b     # Multiplication

print("a:", a)
print("b:", b)
print("a + b =", c)
print("a * b =", d)

