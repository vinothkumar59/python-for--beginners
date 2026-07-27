"""
Variables Solutions

Author : Vinoth Kumar
"""

# ==========================================
# Solution 1
# Create a variable called company and print it.
# ==========================================

company = "OpenAI"
print(company)

# ==========================================
# Solution 2
# Create variables for name, age and city.
# ==========================================

name = "Vinoth"
age = 28
city = "Chennai"

print(name)
print(age)
print(city)

# ==========================================
# Solution 3
# Swap two variables.
# ==========================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# ==========================================
# Solution 4
# Print the type of three variables.
# ==========================================

name = "Python"
age = 30
salary = 55000.50

print(type(name))
print(type(age))
print(type(salary))

# ==========================================
# Solution 5
# Create global and local variables.
# ==========================================

company = "OpenAI"

def employee():
    employee_name = "Rahul"

    print(company)
    print(employee_name)

employee()

# ==========================================
# Solution 6
# Create multiple variables in one line.
# ==========================================

name, age, city = "Vinoth", 28, "Chennai"

print(name)
print(age)
print(city)

# ==========================================
# Solution 7
# Delete a variable using del.
# ==========================================

number = 100

print(number)

del number

# Uncomment to see NameError
# print(number)

# ==========================================
# Solution 8
# Print id() of two variables.
# ==========================================

x = 10
y = 20

print(id(x))
print(id(y))

# ==========================================
# Solution 9
# Assign one value to three variables.
# ==========================================

x = y = z = 100

print(x)
print(y)
print(z)

# ==========================================
# Solution 10
# Create valid and invalid variable names.
# ==========================================

employee_name = "Rahul"
employeeSalary = 50000
_employee = 101

print(employee_name)
print(employeeSalary)
print(_employee)

# Invalid Variable Names (Examples)

# 2employee = "Rahul"
# employee-name = "Rahul"
# class = "Python"