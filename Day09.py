# Set
numbers = {15, 25, 35}
names = {"Aman", "Priya", "Kiran"}
mixed = {10, "Python", 7.5, False}
print(numbers)
s = set()  # Creating an empty set
print(s)
# Duplicate values are automatically removed
data = {10, 20, 30, 20, 10}
print(data)
# Membership Operators
data = {10, 20, 30}
print(20 in data)
print(50 not in data)
# Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
# Intersection
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)
# Difference
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)
# Symmetric Difference
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)
# Subset
a = {1, 2}
b = {1, 2, 3, 4}
print(a <= b)
# Superset
a = {1, 2, 3, 4}
b = {1, 2}
print(a >= b)
# Dictionaries
data = {}  # Empty dictionary
data = dict()


# Accessing values

student = {
    "name": "Arjun",
    "age": 21
}

print(student["name"])
print(student["age"])


# Updating a value

student = {
    "name": "Arjun",
    "age": 21
}

student["age"] = 22

print(student)
# Adding a new key-value pair
student = {
    "name": "Arjun"
}
student["course"] = "Python"
print(student)
# Removing items
student = {
    "name": "Arjun",
    "age": 21
}
del student["age"]
print(student)
# Membership Operators
student = {
    "name": "Arjun",
    "age": 21
}
print("name" in student)
print("course" not in student)
