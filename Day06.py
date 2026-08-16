# Input Formatting

name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))
print(age)

salary = float(input("Enter your monthly salary: "))
print(salary)

skills = input("Enter your skills (space-separated): ").split()
print(skills)

hobbies = input("Enter your hobbies (comma-separated): ").split(',')
print(hobbies)

marks = list(map(int, input("Enter subject marks: ").split()))
print(marks)

prices = list(map(float, input("Enter product prices: ").split()))
print(prices)

dimensions = tuple(map(int, input("Enter room dimensions: ").split()))
print(dimensions)

student_ids = set(map(int, input("Enter student IDs: ").split()))
print(student_ids)

student = eval(input("Enter student details as a dictionary: "))
print(student)

username, password = input("Enter username and password: ").split()

print("Username:", username)
print("Password:", password)


# Output Formatting

print("Welcome to Python!")

name = "Rahul"
age = 21

print("Name:", name, "Age:", age)

print("2026", "08", "16", sep="-")

print("Hello", end=" ")
print("Python")

print("Python\nProgramming")

print("Name:\tRahul")

name = "Rahul"
age = 21
marks = 87.5

print("Name:", name, "Age:", age, "Marks:", marks)


# % Formatting

name = "Rahul"
age = 21
marks = 87.568

print("Name: %s | Age: %d | Marks: %.2f" % (name, age, marks))


# f-string Formatting

name = "Sneha"
age = 22
marks = 91.678

print(f"Name: {name} | Age: {age} | Marks: {marks:.2f}")


# format() Method

name = "Arjun"
age = 23
marks = 89.456

print("Name: {} | Age: {} | Marks: {:.1f}".format(name, age, marks))
