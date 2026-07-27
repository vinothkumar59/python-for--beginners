"""
Topic : Lambda Functions

Author : Vinoth Kumar
"""

from functools import reduce

print("=" * 50)
print("LAMBDA")
print("=" * 50)

square = lambda x: x * x

print(square(5))

print("=" * 50)
print("ADD")
print("=" * 50)

add = lambda a, b: a + b

print(add(10, 20))

print("=" * 50)
print("MAP")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

print("=" * 50)
print("FILTER")
print("=" * 50)

numbers = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

print("=" * 50)
print("REDUCE")
print("=" * 50)

numbers = [10, 20, 30, 40]

result = reduce(lambda x, y: x + y, numbers)

print(result)

print("=" * 50)
print("SORTED")
print("=" * 50)

employees = [
    ("Rahul", 45000),
    ("Vinoth", 70000),
    ("Arun", 55000)
]

result = sorted(employees, key=lambda x: x[1])

print(result)

print("=" * 50)
print("MAX")
print("=" * 50)

print(max(employees, key=lambda x: x[1]))

print("=" * 50)
print("MIN")
print("=" * 50)

print(min(employees, key=lambda x: x[1]))

print("=" * 50)
print("LAMBDA COMPLETED")
print("=" * 50)