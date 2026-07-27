"""
Topic : If Else

Author : Vinoth Kumar
"""

print("=" * 50)
print("IF")
print("=" * 50)

age = 20

if age >= 18:
    print("Eligible to Vote")

print("=" * 50)
print("IF ELSE")
print("=" * 50)

salary = 45000

if salary >= 50000:
    print("High Salary")
else:
    print("Low Salary")

print("=" * 50)
print("IF ELIF ELSE")
print("=" * 50)

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

print("=" * 50)
print("NESTED IF")
print("=" * 50)

age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Citizen Required")
else:
    print("Under Age")

print("=" * 50)
print("AND")
print("=" * 50)

experience = 5
degree = True

if experience >= 3 and degree:
    print("Selected")

print("=" * 50)
print("OR")
print("=" * 50)

python_skill = False
sql_skill = True

if python_skill or sql_skill:
    print("Eligible for Interview")

print("=" * 50)
print("NOT")
print("=" * 50)

active = False

if not active:
    print("Inactive User")

print("=" * 50)
print("TERNARY OPERATOR")
print("=" * 50)

age = 22

result = "Adult" if age >= 18 else "Minor"

print(result)

print("=" * 50)
print("IF ELSE COMPLETED")
print("=" * 50)