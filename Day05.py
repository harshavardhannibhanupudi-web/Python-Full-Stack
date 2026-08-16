# Operators in Python

# Arithmetic Operators
price = 500
quantity = 4
print(price + quantity)
print(price - quantity)
print(price * quantity)
print(price / quantity)
apples = 57
box_capacity = 10
print(apples // box_capacity)   # Complete boxes
print(apples % box_capacity)    # Remaining apples

# Assignment Operators

salary = 25000
salary += 5000
print(salary)
expenses = 8000
expenses -= 2000
print(expenses)

# Comparison Operators

marks = 75
pass_marks = 40
print(marks > pass_marks)
print(marks == pass_marks)
print(marks != pass_marks)
print(marks >= 60)

# Logical Operators

age = 22
has_id = True
print(age >= 18 and has_id)

# Bitwise Operators

x = 10
y = 15
print(x & y)
print(x | y)
print(x ^ y)
print(x << 2)
print(x >> 2)

# Membership Operators

languages = ["Python", "Java", "C++"]
print("Python" in languages)
print("JavaScript" in languages)
print("JavaScript" not in languages)

# Identity Operators

a = 10
b = 10
print(a is b)
x = [10, 20]
y = [10, 20]
print(x == y)   # Same values
print(x is y)   # Different objects
