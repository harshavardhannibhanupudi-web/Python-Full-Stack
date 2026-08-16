# Conditional Statements
# If Statement
number = 15
if number > 10:
    print("Number is greater than 10")
print("Program End")
number = 8
if number > 10:
    print("Number is greater than 10")
print("Program End")
# If-Else Statement
items = 10
if items > 0:
    print("Items are available")
else:
    print("Out of stock")
age = int(input("Enter your age: "))
if age >= 18:
    print("You can apply for a driving license")
else:
    print("You cannot apply for a driving license")
# Check Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Find Largest Number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is larger")
else:
    print("Second number is larger")


# Grade Calculation

marks = 76

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Positive, Negative or Zero

number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Electricity Bill

units = 180

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
elif units <= 500:
    bill = units * 4
else:
    bill = units * 6

print("Electricity Bill:", bill)


# Nested If - Login

username = "user"
password = "pass123"

if username == "user":
    if password == "pass123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")


# Nested If - ATM Withdrawal

balance = 15000
amount = 7000

if amount > 0:
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid Amount")