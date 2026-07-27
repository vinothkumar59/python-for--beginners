"""
Topic : Variables
Author : Vinoth Kumar

Variables are used to store data in memory.
"""

# Integer
age = 28

# Float
salary = 45000.75

# String
name = "Vinoth"

# Boolean
is_employee = True

print(age)
print(salary)
print(name)
print(is_employee)

# Valid variable names

employee_name = "Rahul"

employeeSalary = 60000

employee_salary = 70000

EMPLOYEE_ID = 101


# Invalid

# 1employee = 10

# employee-name = "Rahul"

# class = "Python"

# Multiply Assignment

x = y = z = 100

print(x)
print(y)
print(z)

# Multiply Variable

name, age, city = "Vinoth", 28, "Chennai"

print(name)
print(age)
print(city)

# Delete Variable

number = 100

print(number)

del number

# print(number)

# Type Checking

name = "Python"

print(type(name))

age = 30

print(type(age))

salary = 50000.50

print(type(salary))

# Variable Swapping

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Global Variable

company = "OpenAI"


def display():

    print(company)


display()

# Local Variable

def employee():

    employee_name = "Rahul"

    print(employee_name)


employee()

# Interview Questions

# 1. What is a variable?

# 2. Difference between local and global variable?

# 3. What is dynamic typing?

# 4. Explain multiple assignment.

# 5. What does del do?

# 6. What is type()?

# 7. What are variable naming rules?

# 8. Difference between = and == ?

# 9. Can Python change variable type at runtime?

# 10. Explain variable swapping.

