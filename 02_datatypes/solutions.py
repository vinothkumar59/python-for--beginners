"""
Data Types Solutions
"""

age = 28
salary = 45000.75
number = 3 + 5j
status = True
name = "Vinoth"

languages = ["Python", "SQL", "Java"]

cities = ("Chennai", "Delhi", "Mumbai")

employee = {
    "id": 101,
    "name": "Vinoth"
}

numbers = {10, 20, 30}

data = None

print(float(age))
print(int(salary))
print(tuple(languages))
print(list(cities))
print(type(employee))
print(isinstance(age, int))
print(id(age))