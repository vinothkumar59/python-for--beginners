"""
Topic : Data Types

Author : Vinoth Kumar

Description :
Examples of Python Built-in Data Types
"""

print("=" * 50)
print("INTEGER")
print("=" * 50)

age = 28

print(age)
print(type(age))

print("=" * 50)
print("FLOAT")
print("=" * 50)

salary = 45000.75

print(salary)
print(type(salary))

print("=" * 50)
print("COMPLEX")
print("=" * 50)

number = 3 + 5j

print(number)
print(type(number))

print("=" * 50)
print("BOOLEAN")
print("=" * 50)

is_employee = True

print(is_employee)
print(type(is_employee))

print("=" * 50)
print("STRING")
print("=" * 50)

name = "Vinoth"

print(name)
print(type(name))

print("=" * 50)
print("LIST")
print("=" * 50)

languages = ["Python", "Java", "SQL", "PySpark"]

print(languages)
print(type(languages))

print("=" * 50)
print("TUPLE")
print("=" * 50)

cities = ("Chennai", "Bangalore", "Delhi")

print(cities)
print(type(cities))

print("=" * 50)
print("DICTIONARY")
print("=" * 50)

employee = {
    "employee_id": 101,
    "employee_name": "Vinoth",
    "department": "Data Engineering",
    "salary": 50000
}

print(employee)
print(type(employee))

print("=" * 50)
print("SET")
print("=" * 50)

numbers = {10, 20, 30, 40, 50}

print(numbers)
print(type(numbers))

print("=" * 50)
print("NONE")
print("=" * 50)

data = None

print(data)
print(type(data))

print("=" * 50)
print("TYPE CONVERSION")
print("=" * 50)

number = 100

print(float(number))

salary = 50000.75

print(int(salary))

age = 25

print(str(age))

text = "123"

print(int(text))

marks = [90, 80, 70]

print(tuple(marks))

cities = ("Chennai", "Mumbai")

print(list(cities))

numbers = [1, 2, 2, 3, 4, 4]

print(set(numbers))

print("=" * 50)
print("ISINSTANCE")
print("=" * 50)

print(isinstance(100, int))
print(isinstance(10.5, float))
print(isinstance("Python", str))
print(isinstance([1, 2], list))
print(isinstance((1, 2), tuple))
print(isinstance({"a": 1}, dict))
print(isinstance({1, 2}, set))

print("=" * 50)
print("ID FUNCTION")
print("=" * 50)

x = 100
y = 100

print(id(x))
print(id(y))

print("=" * 50)
print("SUMMARY")
print("=" * 50)

print("int")
print("float")
print("complex")
print("bool")
print("str")
print("list")
print("tuple")
print("dict")
print("set")
print("NoneType")

print("=" * 50)
print("DATA TYPES COMPLETED SUCCESSFULLY")
print("=" * 50)