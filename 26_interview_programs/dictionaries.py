"""
Topic : Dictionary Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("DICTIONARY INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Merge Dictionaries
# ----------------------------------------------------

print("\n1. Merge Dictionaries")

dict1 = {
    "id": 101,
    "name": "Vinoth"
}

dict2 = {
    "department": "Data Engineering",
    "salary": 60000
}

merged = dict1 | dict2

print(merged)

# ----------------------------------------------------
# 2 Character Frequency
# ----------------------------------------------------

print("\n2. Character Frequency")

text = "programming"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

print(frequency)

# ----------------------------------------------------
# 3 Maximum Value
# ----------------------------------------------------

print("\n3. Maximum Value")

marks = {
    "Math": 85,
    "Science": 95,
    "English": 78
}

print(max(marks.values()))

# ----------------------------------------------------
# 4 Sort Dictionary
# ----------------------------------------------------

print("\n4. Sort Dictionary")

employee = {
    "c": 300,
    "a": 100,
    "b": 200
}

sorted_dict = dict(sorted(employee.items()))

print(sorted_dict)

# ----------------------------------------------------
# 5 Reverse Key-Value
# ----------------------------------------------------

print("\n5. Reverse Key-Value")

employee = {
    "id": 101,
    "name": "Vinoth",
    "city": "Chennai"
}

reverse = {}

for key, value in employee.items():

    reverse[value] = key

print(reverse)

print("\n" + "=" * 60)
print("DICTIONARY PROGRAMS COMPLETED")
print("=" * 60)