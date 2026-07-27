"""
Topic : Functions

Author : Vinoth Kumar
"""

print("=" * 50)
print("FUNCTIONS")
print("=" * 50)

# ------------------------------------------
# Simple Function
# ------------------------------------------

def greet():
    print("Welcome to Python")

greet()

# ------------------------------------------
# Function with Parameter
# ------------------------------------------

def display_name(name):
    print(name)

display_name("Vinoth")

# ------------------------------------------
# Function with Multiple Parameters
# ------------------------------------------

def employee(name, department):
    print(name)
    print(department)

employee("Vinoth", "Data Engineering")

# ------------------------------------------
# Return Statement
# ------------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# ------------------------------------------
# Default Parameter
# ------------------------------------------

def country(name="India"):
    print(name)

country()

country("USA")

# ------------------------------------------
# Keyword Arguments
# ------------------------------------------

def student(name, age):
    print(name)
    print(age)

student(age=28, name="Vinoth")

# ------------------------------------------
# *args
# ------------------------------------------

def total(*numbers):
    print(sum(numbers))

total(10,20,30,40)

# ------------------------------------------
# **kwargs
# ------------------------------------------

def details(**employee):

    for key,value in employee.items():
        print(key, value)

details(
    name="Vinoth",
    city="Chennai",
    salary=60000
)

# ------------------------------------------
# Scope
# ------------------------------------------

company = "OpenAI"

def show_company():
    print(company)

show_company()

# ------------------------------------------
# Recursive Function
# ------------------------------------------

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))

print("=" * 50)
print("FUNCTIONS COMPLETED")
print("=" * 50)