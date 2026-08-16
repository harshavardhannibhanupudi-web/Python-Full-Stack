# For Loop
# Printing odd numbers from 1 to 15
for i in range(1, 16):
    if i % 2 != 0:
        print(i)

# Checking numbers from 1 to 7

for i in range(1, 8):
    if i % 2 == 0:
        print(i)
    print("Checking next number")
print("Loop completed")
# Factorial of a number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial:", factorial)
# Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)