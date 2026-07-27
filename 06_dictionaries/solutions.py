employee = {
    "id":101,
    "name":"Vinoth",
    "salary":50000
}

print(employee["name"])

employee["city"] = "Chennai"

employee["salary"] = 70000

print(employee.keys())

print(employee.values())

print(employee.items())

employee.pop("city")

employee.popitem()

copy_dict = employee.copy()

print(copy_dict)

copy_dict.clear()

print(copy_dict)

for key,value in employee.items():
    print(key,value)

print(len(employee))