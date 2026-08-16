# For Loop
# Print multiples of 3 from 1 to 20
for num in range(1, 21):
    if num % 3 == 0:
        print(num)
# Check numbers from 1 to 8
for num in range(1, 9):
    if num % 2 != 0:
        print(num)
    print("Checking:", num)
print("Loop Finished")
# Factorial of a number
number = int(input("Enter a number: "))
result = 1
for value in range(1, number + 1):
    result *= value
print("Factorial of", number, "is", result)
# Multiplication table
number = int(input("Enter a number: "))
for count in range(1, 13):
    print(f"{number} x {count} = {number * count}")