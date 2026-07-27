"""
Topic : Pattern Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("PATTERN INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Square Pattern
# ----------------------------------------------------

print("\n1. Square Pattern")

for i in range(5):
    print("* " * 5)

# ----------------------------------------------------
# 2 Left Triangle
# ----------------------------------------------------

print("\n2. Left Triangle")

for i in range(1, 6):
    print("* " * i)

# ----------------------------------------------------
# 3 Pyramid Pattern
# ----------------------------------------------------

print("\n3. Pyramid Pattern")

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

# ----------------------------------------------------
# 4 Number Pattern
# ----------------------------------------------------

print("\n4. Number Pattern")

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

# ----------------------------------------------------
# 5 Floyd's Triangle
# ----------------------------------------------------

print("\n5. Floyd's Triangle")

number = 1

for i in range(1, 6):

    for j in range(i):

        print(number, end=" ")

        number += 1

    print()

print("\n" + "=" * 60)
print("PATTERN PROGRAMS COMPLETED")
print("=" * 60)