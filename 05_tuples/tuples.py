"""
Topic : Tuples

Author : Vinoth Kumar
"""

print("=" * 50)
print("TUPLE")
print("=" * 50)

numbers = (10, 20, 30, 40, 50)

print(numbers)

print("=" * 50)
print("INDEXING")
print("=" * 50)

print(numbers[0])
print(numbers[-1])

print("=" * 50)
print("SLICING")
print("=" * 50)

print(numbers[1:4])

print("=" * 50)
print("COUNT")
print("=" * 50)

values = (10, 20, 20, 30, 20)

print(values.count(20))

print("=" * 50)
print("INDEX")
print("=" * 50)

print(values.index(30))

print("=" * 50)
print("LENGTH")
print("=" * 50)

print(len(numbers))

print("=" * 50)
print("NESTED TUPLE")
print("=" * 50)

employee = (
    101,
    "Vinoth",
    ("Python", "SQL", "PySpark")
)

print(employee)

print("=" * 50)
print("PACKING")
print("=" * 50)

person = ("Vinoth", 28, "Chennai")

print(person)

print("=" * 50)
print("UNPACKING")
print("=" * 50)

name, age, city = person

print(name)
print(age)
print(city)

print("=" * 50)
print("ITERATION")
print("=" * 50)

for value in numbers:
    print(value)

print("=" * 50)
print("MEMBERSHIP")
print("=" * 50)

print(30 in numbers)
print(100 in numbers)

print("=" * 50)
print("TUPLE COMPLETED")
print("=" * 50)