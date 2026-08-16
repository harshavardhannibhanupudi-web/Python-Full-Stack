# Operations on Strings
# Concatenation
first_name = "Harsha"
last_name = "Vardhan"
full_name = first_name + " " + last_name
print(full_name)
# Repetition
print("Python " * 3)
# Indexing
language = "Python"
print(language[0])    # First character
print(language[-1])   # Last character
# Slicing
print(language[0:2])  # Characters from index 0 to 1
print(language[:4])   # From beginning to index 3
print(language[2:])   # From index 2 to end
# Membership
print("Py" in language)
print("Java" not in language)
# Built-in String Functions
# 1. len()
message = "Hello Python"
print(len(message))
# 2. max() and min()
print(max("python"))
print(min("python"))

# 3. sorted()
print(sorted("developer"))

# 4. ord() and chr()
print(ord('B'))
print(chr(98))