"""
Topic : Number Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("NUMBER INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Reverse Number
# ----------------------------------------------------

print("\n1. Reverse Number")

number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print(reverse)

# ----------------------------------------------------
# 2 Palindrome Number
# ----------------------------------------------------

print("\n2. Palindrome Number")

number = 121

temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if number == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# ----------------------------------------------------
# 3 Prime Number
# ----------------------------------------------------

print("\n3. Prime Number")

number = 17

prime = True

for i in range(2, number):

    if number % i == 0:
        prime = False
        break

if prime:
    print("Prime")
else:
    print("Not Prime")

# ----------------------------------------------------
# 4 Fibonacci Series
# ----------------------------------------------------

print("\n4. Fibonacci Series")

first = 0
second = 1

for i in range(10):

    print(first, end=" ")

    first, second = second, first + second

print()

# ----------------------------------------------------
# 5 Factorial
# ----------------------------------------------------

print("\n5. Factorial")

number = 5

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)

# ----------------------------------------------------
# 6 Armstrong Number
# ----------------------------------------------------

print("\n6. Armstrong Number")

number = 153

temp = number

total = 0

while temp > 0:

    digit = temp % 10

    total += digit ** 3

    temp //= 10

if total == number:
    print("Armstrong")
else:
    print("Not Armstrong")

# ----------------------------------------------------
# 7 Perfect Number
# ----------------------------------------------------

print("\n7. Perfect Number")

number = 28

total = 0

for i in range(1, number):

    if number % i == 0:
        total += i

if total == number:
    print("Perfect")
else:
    print("Not Perfect")

# ----------------------------------------------------
# 8 Even or Odd
# ----------------------------------------------------

print("\n8. Even or Odd")

number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# ----------------------------------------------------
# 9 Leap Year
# ----------------------------------------------------

print("\n9. Leap Year")

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# ----------------------------------------------------
# 10 Swap Two Numbers
# ----------------------------------------------------

print("\n10. Swap Two Numbers")

a = 10
b = 20

print("Before Swap :", a, b)

a, b = b, a

print("After Swap  :", a, b)

print("\n" + "=" * 60)
print("NUMBER PROGRAMS COMPLETED")
print("=" * 60)