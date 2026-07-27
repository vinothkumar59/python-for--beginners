"""
Topic : Exception Handling

Author : Vinoth Kumar
"""

print("=" * 50)
print("TRY EXCEPT")
print("=" * 50)

try:
    print(10 / 0)

except ZeroDivisionError as error:
    print(error)

print("=" * 50)
print("VALUE ERROR")
print("=" * 50)

try:
    number = int("Python")

except ValueError as error:
    print(error)

print("=" * 50)
print("INDEX ERROR")
print("=" * 50)

numbers = [10,20,30]

try:
    print(numbers[5])

except IndexError as error:
    print(error)

print("=" * 50)
print("KEY ERROR")
print("=" * 50)

employee = {"name":"Vinoth"}

try:
    print(employee["salary"])

except KeyError as error:
    print(error)

print("=" * 50)
print("FILE NOT FOUND")
print("=" * 50)

try:
    with open("abc.txt","r") as file:
        print(file.read())

except FileNotFoundError as error:
    print(error)

print("=" * 50)
print("ELSE")
print("=" * 50)

try:
    print(100/10)

except ZeroDivisionError:
    print("Error")

else:
    print("Executed Successfully")

print("=" * 50)
print("FINALLY")
print("=" * 50)

try:
    print("Database Connected")

finally:
    print("Connection Closed")

print("=" * 50)
print("RAISE")
print("=" * 50)

age = 15

try:

    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as error:
    print(error)

print("=" * 50)
print("MULTIPLE EXCEPT")
print("=" * 50)

try:
    number = int("ABC")
    print(10/0)

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division Error")

print("=" * 50)
print("EXCEPTION HANDLING COMPLETED")
print("=" * 50)