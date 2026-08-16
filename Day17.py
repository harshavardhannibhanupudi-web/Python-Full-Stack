# Day 17 - Scope and Functional Programming
# 1. Local Scope
def show_name():
    name = "Harsha"
    print("Local:", name)
show_name()
# 2. Global Scope
college = "CMR Institute"
def show_college():
    print("Global:", college)
show_college()
# 3. global Keyword
count = 10
def update_count():
    global count
    count += 5
update_count()
print("Updated count:", count)
# 4. Non-Local Scope
def outer_function():
    message = "Hello"
    def inner_function():
        nonlocal message
        message = "Hello Python"

    inner_function()
    print("Non-local:", message)


outer_function()


# 5. Built-in Scope

numbers = [12, 45, 23, 67]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Total:", sum(numbers))


# 6. Lambda Function

square = lambda x: x * x

print("Square:", square(6))


# 7. map()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Squares:", squares)


# 8. filter()

numbers = [10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)


# 9. reduce()

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print("Product:", product)


# 10. LEGB Example

value = "Global"

def outer():
    value = "Enclosing"

    def inner():
        value = "Local"
        print(value)

    inner()


outer()