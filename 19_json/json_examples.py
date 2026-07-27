"""
Topic : JSON

Author : Vinoth Kumar
"""

import json

print("=" * 50)
print("PYTHON TO JSON STRING")
print("=" * 50)

employee = {
    "id":101,
    "name":"Vinoth",
    "department":"Data Engineering",
    "salary":60000
}

json_data = json.dumps(employee, indent=4)

print(json_data)

print("=" * 50)
print("JSON STRING TO PYTHON")
print("=" * 50)

text = '''
{
    "id":102,
    "name":"Rahul",
    "city":"Chennai"
}
'''

data = json.loads(text)

print(data)
print(type(data))

print("=" * 50)
print("WRITE JSON FILE")
print("=" * 50)

with open("employee.json","w") as file:
    json.dump(employee,file,indent=4)

print("JSON File Created")

print("=" * 50)
print("READ JSON FILE")
print("=" * 50)

with open("employee.json","r") as file:
    data = json.load(file)

print(data)

print("=" * 50)
print("ACCESS JSON VALUES")
print("=" * 50)

print(data["name"])
print(data["salary"])

print("=" * 50)
print("NESTED JSON")
print("=" * 50)

company = {
    "company":"OpenAI",
    "employee":{
        "id":101,
        "name":"Vinoth",
        "city":"Chennai"
    }
}

print(company["employee"]["name"])

print("=" * 50)
print("JSON COMPLETED")
print("=" * 50)