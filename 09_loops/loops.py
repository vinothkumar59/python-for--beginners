"""
Topic : Loops

Author : Vinoth Kumar
"""

print("=" * 50)
print("FOR LOOP")
print("=" * 50)

for i in range(1, 6):
    print(i)

print("=" * 50)
print("WHILE LOOP")
print("=" * 50)

count = 1

while count <= 5:
    print(count)
    count += 1

print("=" * 50)
print("BREAK")
print("=" * 50)

for i in range(1, 11):

    if i == 6:
        break

    print(i)

print("=" * 50)
print("CONTINUE")
print("=" * 50)

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)

print("=" * 50)
print("PASS")
print("=" * 50)

for i in range(1, 6):

    if i == 3:
        pass

    print(i)

print("=" * 50)
print("NESTED LOOP")
print("=" * 50)

for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)

print("=" * 50)
print("RANGE")
print("=" * 50)

for i in range(5):
    print(i)

print("=" * 50)
print("ENUMERATE")
print("=" * 50)

languages = ["Python", "SQL", "PySpark"]

for index, value in enumerate(languages):

    print(index, value)

print("=" * 50)
print("ZIP")
print("=" * 50)

names = ["A", "B", "C"]

marks = [90, 80, 70]

for name, mark in zip(names, marks):

    print(name, mark)

print("=" * 50)
print("LOOP THROUGH STRING")
print("=" * 50)

text = "Python"

for char in text:

    print(char)

print("=" * 50)
print("LOOP THROUGH LIST")
print("=" * 50)

numbers = [10, 20, 30]

for number in numbers:

    print(number)

print("=" * 50)
print("SUM USING LOOP")
print("=" * 50)

total = 0

for i in range(1, 6):

    total += i

print(total)

print("=" * 50)
print("LOOPS COMPLETED")
print("=" * 50)