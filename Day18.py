# Day 18 - Recursion
# 1.Fibonacci series
def fibbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)
n=int(input())
r=fibbo(n)
print(f"the factorial of {n} is {r}")
# 2. Basic Recursion
def print_numbers(n):
    if n == 0:                 # Base Case
        return
    print(n)
    print_numbers(n - 1)       # Recursive Case
print_numbers(n)
# 3. Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial:", factorial(5))
# 4. Sum of Natural Numbers using Recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)
print("Sum:", sum_numbers(5))


