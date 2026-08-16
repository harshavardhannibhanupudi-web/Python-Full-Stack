# Day 14 - Number and Digit Problems
# 1. Counting Digits
num = 58342
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10
print("Number of digits:", count)
# 2. Finding the Middle Digit
num = 58342
temp = num
digits = 0
while temp > 0:
    digits += 1
    temp //= 10
if digits % 2 != 0:
    middle_position = digits // 2
    temp = num
    for i in range(middle_position):
        temp //= 10
    middle_digit = temp % 10
    print("Middle digit:", middle_digit)
else:
    print("Middle digit not available for even number of digits")


# 3. Alternate Digits from the Beginning

num = 58342
digits = str(num)

print("Alternate digits from beginning:")

for i in range(0, len(digits), 2):
    print(digits[i], end=" ")

print()


# 4. Alternate Digits from the End

print("Alternate digits from end:")

for i in range(len(digits) - 1, -1, -2):
    print(digits[i], end=" ")

print()


# 5. Sum of Prime Digits

num = 235467
temp = num
prime_sum = 0

while temp > 0:
    digit = temp % 10

    if digit in (2, 3, 5, 7):
        prime_sum += digit

    temp //= 10

print("Sum of prime digits:", prime_sum)


# 6. Digit Extraction using % and //

num = 7462

print("Extracting digits:")

while num > 0:
    digit = num % 10
    print("Digit:", digit)

    num //= 10