for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(1, 20, 2):
    print(i)

total = 0

for i in range(1, 101):
    total += i

print(total)

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

text = "Python"

print(text[::-1])

numbers = [10, 20, 30]

for value in numbers:
    print(value)

languages = ["Python", "SQL"]

for index, value in enumerate(languages):
    print(index, value)

names = ["A", "B"]

marks = [90, 95]

for name, mark in zip(names, marks):
    print(name, mark)