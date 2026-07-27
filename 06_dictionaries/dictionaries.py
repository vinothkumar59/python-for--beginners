"""
Topic : Dictionaries

Author : Vinoth Kumar
"""

print("=" * 50)
print("DICTIONARY")
print("=" * 50)

employee = {
    "employee_id":101,
    "employee_name":"Vinoth",
    "department":"Data Engineering",
    "salary":60000
}

print(employee)

print("=" * 50)
print("ACCESS VALUE")
print("=" * 50)

print(employee["employee_name"])
print(employee.get("salary"))

print("=" * 50)
print("ADD KEY")
print("=" * 50)

employee["city"] = "Chennai"

print(employee)

print("=" * 50)
print("UPDATE")
print("=" * 50)

employee["salary"] = 70000

print(employee)

print("=" * 50)
print("KEYS")
print("=" * 50)

print(employee.keys())

print("=" * 50)
print("VALUES")
print("=" * 50)

print(employee.values())

print("=" * 50)
print("ITEMS")
print("=" * 50)

print(employee.items())

print("=" * 50)
print("POP")
print("=" * 50)

employee.pop("city")

print(employee)

print("=" * 50)
print("POPITEM")
print("=" * 50)

employee.popitem()

print(employee)

print("=" * 50)
print("COPY")
print("=" * 50)

new_employee = employee.copy()

print(new_employee)

print("=" * 50)
print("CLEAR")
print("=" * 50)

sample = {
    "a":1,
    "b":2
}

sample.clear()

print(sample)

print("=" * 50)
print("ITERATION")
print("=" * 50)

for key,value in employee.items():
    print(key,"=",value)

print("=" * 50)
print("DICTIONARY COMPLETED")
print("=" * 50)