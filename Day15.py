# Functions in Python
# Function without parameters
def welcome():
    print("Welcome to Python Programming!")
welcome()
# Function without parameters
def calculate_sum():
    x = 15
    y = 25
    print("Sum:", x + y)
calculate_sum()
# Function with parameters
def greet_user(name):
    print("Hello", name)
greet_user("Harsha")
# Parameters and Arguments
def multiply(a, b):
    print("Product:", a * b)
multiply(5, 6)
# Positional Arguments
def employee(name, age):
    print("Name:", name)
    print("Age:", age)
employee("Rahul", 24)
# Keyword Arguments
def employee(name, age):
    print("Name:", name)
    print("Age:", age)
employee(age=24, name="Rahul")
# Default Arguments
def welcome(name="Guest"):
    print("Hello", name)
welcome()
welcome("Ananya")
# Variable-Length Arguments - *args
def total(*numbers):
    print("Numbers:", numbers)
    print("Total:", sum(numbers))
total(10, 20, 30, 40)
# Variable-Length Arguments - **kwargs
def profile(**details):
    print(details)
profile(name="Kiran", age=23, city="Hyderabad")
# Positional + Default + Variable-Length Arguments
def employee(name, age=25, *skills):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
employee("Kiran", 23, "Python", "SQL", "Git")
# Return Statement
def multiply(a, b):
    return a * b
result = multiply(7, 8)
print("Result:", result)