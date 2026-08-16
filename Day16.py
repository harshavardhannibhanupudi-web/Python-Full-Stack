# Day 16 - Functions and Arguments
# 1. Function
def welcome():
    print("Welcome to Python!")
welcome()
# 2. Function with Parameters
def greet(name):
    print("Hello", name)
greet("Harsha")
# 3. Positional Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Rahul", 22)
# 4. Keyword Arguments
student(age=23, name="Ananya")
# 5. Default Arguments
def message(name="Guest"):
    print("Hello", name)
message()
message("Kiran")
# 6. *args - Variable-Length Positional Arguments

def calculate_sum(*numbers):
    print("Numbers:", numbers)
    print("Total:", sum(numbers))


calculate_sum(10, 20, 30, 40)


# 7. **kwargs - Variable-Length Keyword Arguments

def show_profile(**details):
    print("Profile:", details)


show_profile(name="Ravi", age=21, city="Hyderabad")


# 8. Return Statement

def multiply(a, b):
    return a * b


result = multiply(5, 6)

print("Result:", result)


# 9. Multiple Return Values

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


add_result, sub_result = calculate(20, 8)

print("Addition:", add_result)
print("Subtraction:", sub_result)


# 10. Function with Different Data Types

def display_data(name, marks, skills, details):
    print("Name:", name)
    print("Marks:", marks)
    print("Skills:", skills)
    print("Details:", details)


display_data(
    "Harsha",
    85,
    ["Python", "SQL"],
    {"city": "Hyderabad", "course": "Python Full Stack"}
)