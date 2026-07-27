"""
Topic : Python Interview Programs

Author : Vinoth Kumar
"""

import logging
import re
from datetime import datetime
from functools import wraps

print("=" * 60)
print("PYTHON INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Exception Handling
# ----------------------------------------------------

print("\n1. Exception Handling")

try:
    print(10 / 0)

except ZeroDivisionError as error:
    print(error)

# ----------------------------------------------------
# 2 Lambda
# ----------------------------------------------------

print("\n2. Lambda")

square = lambda x: x * x

print(square(5))

# ----------------------------------------------------
# 3 List Comprehension
# ----------------------------------------------------

print("\n3. List Comprehension")

numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

print(result)

# ----------------------------------------------------
# 4 Generator
# ----------------------------------------------------

print("\n4. Generator")

def numbers():

    for number in range(1, 6):
        yield number

for value in numbers():
    print(value)

# ----------------------------------------------------
# 5 Decorator
# ----------------------------------------------------

print("\n5. Decorator")

def decorator(function):

    @wraps(function)
    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper


@decorator
def greet():

    print("Welcome")


greet()

# ----------------------------------------------------
# 6 Regex
# ----------------------------------------------------

print("\n6. Regex")

text = "Employee 101 Salary 60000"

print(re.findall(r"\d+", text))

# ----------------------------------------------------
# 7 Datetime
# ----------------------------------------------------

print("\n7. Datetime")

print(datetime.now())

# ----------------------------------------------------
# 8 Logging
# ----------------------------------------------------

print("\n8. Logging")

logging.basicConfig(
    filename="python.log",
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logging.info("Python Program Started")

print("Log Created")

# ----------------------------------------------------
# 9 Modules
# ----------------------------------------------------

print("\n9. Modules")

import math

print(math.sqrt(64))

# ----------------------------------------------------
# 10 OOP Mini Program
# ----------------------------------------------------

print("\n10. OOP")

class Employee:

    def __init__(self, employee_id, name):

        self.employee_id = employee_id
        self.name = name

    def display(self):

        print(self.employee_id)
        print(self.name)


employee = Employee(101, "Vinoth")

employee.display()

print("\n" + "=" * 60)
print("PYTHON PROGRAMS COMPLETED")
print("=" * 60)