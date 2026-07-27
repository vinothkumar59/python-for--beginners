"""
Topic : Generators

Author : Vinoth Kumar
"""

print("=" * 50)
print("GENERATOR")
print("=" * 50)


def numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))

print("=" * 50)
print("FOR LOOP")
print("=" * 50)

generator = numbers()

for number in generator:
    print(number)

print("=" * 50)
print("GENERATOR EXPRESSION")
print("=" * 50)

square = (number ** 2 for number in range(1, 6))

for value in square:
    print(value)

print("=" * 50)
print("LARGE DATA")
print("=" * 50)


def employee_ids():

    for employee_id in range(1001, 1006):
        yield employee_id


for employee in employee_ids():
    print(employee)

print("=" * 50)
print("LIST VS GENERATOR")
print("=" * 50)

list_data = [number for number in range(5)]

generator_data = (number for number in range(5))

print(list_data)

print(generator_data)

print("=" * 50)
print("GENERATOR COMPLETED")
print("=" * 50)