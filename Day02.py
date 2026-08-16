# Day 02 - Python
# Statements, Identifiers, Comments,
# Swapping Two Numbers, Deleting a Variable
# ---------------- STATEMENTS ----------------
# Assignment statement
x = 10
# Function call statement
print("Value of x:", x)

# Conditional statement
if x > 5:
    print("x is big")
# ---------------- IDENTIFIERS ----------------
# Variable names are identifiers
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)
# ---------------- COMMENTS ---------------
# This is a single-line comment
"""
This is a multi-line comment.
It explains multiple lines of code.
"""
# ---------------- SWAPPING TWO NUMBERS ----------------
a = 5
b = 10
print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Using a temporary variable
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)
# ---------------- DELETING A VARIABLE ----------------

x = 100
print("\nBefore deleting:", x)
del x
print("Variable x has been deleted.")
