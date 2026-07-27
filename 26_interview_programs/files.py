"""
Topic : File Interview Programs

Author : Vinoth Kumar
"""

import csv
import json
from pathlib import Path

print("=" * 60)
print("FILE INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Write Text File
# ----------------------------------------------------

print("\n1. Write Text File")

with open("sample.txt", "w") as file:
    file.write("Python\n")
    file.write("Data Engineering\n")

print("File Created")

# ----------------------------------------------------
# 2 Read Text File
# ----------------------------------------------------

print("\n2. Read Text File")

with open("sample.txt", "r") as file:
    print(file.read())

# ----------------------------------------------------
# 3 Read CSV File
# ----------------------------------------------------

print("\n3. Read CSV File")

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name", "salary"])

    writer.writerow([101, "Vinoth", 60000])

    writer.writerow([102, "Rahul", 50000])

with open("employees.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ----------------------------------------------------
# 4 Read JSON File
# ----------------------------------------------------

print("\n4. Read JSON File")

employee = {
    "id": 101,
    "name": "Vinoth",
    "salary": 60000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

with open("employee.json", "r") as file:
    data = json.load(file)

print(data)

# ----------------------------------------------------
# 5 Count Lines in File
# ----------------------------------------------------

print("\n5. Count Lines")

path = Path("sample.txt")

with path.open("r") as file:
    count = len(file.readlines())

print("Total Lines :", count)

print("\n" + "=" * 60)
print("FILE PROGRAMS COMPLETED")
print("=" * 60)