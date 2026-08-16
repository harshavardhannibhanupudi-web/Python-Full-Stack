# Set Datatype

student_ids = {101, 102, 103, 104}
print(student_ids)
student_ids = {101, 102, 103, 104}
print(type(student_ids))
student_ids = {101, 102, 103, 101}
print(student_ids)  # Duplicate values are removed
s = set()
print(s)  # Empty set
fruits = {"Apple", "Mango"}
fruits.add("Orange")
print(fruits)  # Adding new element to set

# Dictionaries

student = {
    "name": "Raju",
    "age": 21,
    "city": "Hyderabad"
}
print(student)
print(student["name"])  # Accessing value using key
print(student.get("age"))  # Accessing value using get() method

# Typecasting

x = 10  # Int
y = float(x)  # Converting int to float
print(y, type(y))
c = str(x)  # Converting int to string
print(c, type(c))
d = bool(x)  # Converting int to boolean
print(d, type(d))

# List of Tuples to Dictionary

d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
student_dict = dict(d)
print(student_dict)