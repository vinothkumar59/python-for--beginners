"""
Topic : Set Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("SET INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Union
# ----------------------------------------------------

print("\n1. Union")

set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.union(set2))

# ----------------------------------------------------
# 2 Intersection
# ----------------------------------------------------

print("\n2. Intersection")

print(set1.intersection(set2))

# ----------------------------------------------------
# 3 Difference
# ----------------------------------------------------

print("\n3. Difference")

print(set1.difference(set2))

# ----------------------------------------------------
# 4 Symmetric Difference
# ----------------------------------------------------

print("\n4. Symmetric Difference")

print(set1.symmetric_difference(set2))

# ----------------------------------------------------
# 5 Remove Duplicates from List
# ----------------------------------------------------

print("\n5. Remove Duplicates from List")

numbers = [10, 20, 20, 30, 30, 40, 50, 50]

unique_numbers = list(set(numbers))

print(unique_numbers)

print("\n" + "=" * 60)
print("SET PROGRAMS COMPLETED")
print("=" * 60)