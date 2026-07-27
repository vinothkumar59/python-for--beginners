"""
Topic : Patterns

Author : Vinoth Kumar
"""

print("=" * 50)
print("SQUARE STAR")
print("=" * 50)

for i in range(5):
    print("* " * 5)

print("=" * 50)
print("LEFT TRIANGLE")
print("=" * 50)

for i in range(1, 6):
    print("* " * i)

print("=" * 50)
print("INVERTED TRIANGLE")
print("=" * 50)

for i in range(5, 0, -1):
    print("* " * i)

print("=" * 50)
print("RIGHT TRIANGLE")
print("=" * 50)

for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)

print("=" * 50)
print("PYRAMID")
print("=" * 50)

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

print("=" * 50)
print("INVERTED PYRAMID")
print("=" * 50)

for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)

print("=" * 50)
print("NUMBER TRIANGLE")
print("=" * 50)

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print("=" * 50)
print("SAME NUMBER")
print("=" * 50)

for i in range(1, 6):

    for j in range(i):
        print(i, end=" ")

    print()

print("=" * 50)
print("ALPHABET PATTERN")
print("=" * 50)

for i in range(65, 70):

    for j in range(65, i + 1):
        print(chr(j), end=" ")

    print()

print("=" * 50)
print("FLOYD'S TRIANGLE")
print("=" * 50)

number = 1

for i in range(1, 6):

    for j in range(i):
        print(number, end=" ")

        number += 1

    print()

print("=" * 50)
print("PATTERNS COMPLETED")
print("=" * 50)