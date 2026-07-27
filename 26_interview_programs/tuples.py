"""
Topic : Tuple Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("TUPLE INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Find Maximum
# ----------------------------------------------------

print("\n1. Find Maximum")

numbers = (10, 45, 23, 89, 12)

print(max(numbers))

# ----------------------------------------------------
# 2 Find Minimum
# ----------------------------------------------------

print("\n2. Find Minimum")

print(min(numbers))

# ----------------------------------------------------
# 3 Count Occurrences
# ----------------------------------------------------

print("\n3. Count Occurrences")

numbers = (10, 20, 20, 30, 20, 40)

print(numbers.count(20))

# ----------------------------------------------------
# 4 Find Index
# ----------------------------------------------------

print("\n4. Find Index")

numbers = (10, 20, 30, 40, 50)

print(numbers.index(30))

# ----------------------------------------------------
# 5 Tuple Unpacking
# ----------------------------------------------------

print("\n5. Tuple Unpacking")

employee = (101, "Vinoth", "Data Engineering")

employee_id, name, department = employee

print(employee_id)
print(name)
print(department)

print("\n" + "=" * 60)
print("TUPLE PROGRAMS COMPLETED")
print("=" * 60)