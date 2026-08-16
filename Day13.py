# Day 13 - Loops, Control Statements, Functions and Assertions
# 1. For Loop with Else
for number in range(1, 6):
    print("Number:", number)
else:
    print("For loop completed")
# 2. While Loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
# 3. While Loop with Else
count = 1
while count <= 3:
    print("Value:", count)
    count += 1
else:
    print("While loop completed")
# 4. Break Statement
for number in range(1, 10):
    if number == 5:
        break
    print(number)
print("Loop stopped")
# 5. Continue Statement
for number in range(1, 8):
    if number == 4:
        continue
    print(number)
# 6. Pass Statement
for number in range(1, 4):
    if number == 2:
        pass
    print(number)
# 7. Return Statement
def calculate_square(number):
    return number * number
result = calculate_square(6)
print("Square:", result)
# 8. Assertion Statement
age = 21
assert age >= 18, "Age must be 18 or above"
print("Age condition is valid")