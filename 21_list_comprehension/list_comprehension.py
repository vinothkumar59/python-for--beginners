"""
Topic : List Comprehension

Author : Vinoth Kumar
"""

print("=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

print(result)

print("=" * 50)
print("SQUARE")
print("=" * 50)

square = [number ** 2 for number in numbers]

print(square)

print("=" * 50)
print("EVEN NUMBERS")
print("=" * 50)

even = [number for number in numbers if number % 2 == 0]

print(even)

print("=" * 50)
print("ODD NUMBERS")
print("=" * 50)

odd = [number for number in numbers if number % 2 != 0]

print(odd)

print("=" * 50)
print("UPPERCASE")
print("=" * 50)

names = ["python", "sql", "pyspark"]

upper = [name.upper() for name in names]

print(upper)

print("=" * 50)
print("STRING LENGTH")
print("=" * 50)

length = [len(name) for name in names]

print(length)

print("=" * 50)
print("CONDITIONAL EXPRESSION")
print("=" * 50)

labels = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(labels)

print("=" * 50)
print("NESTED LOOP")
print("=" * 50)

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]

print(pairs)

print("=" * 50)
print("LIST COMPREHENSION COMPLETED")
print("=" * 50)