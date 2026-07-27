import json

employee = {
    "id":101,
    "name":"Vinoth"
}

print(json.dumps(employee))

with open("employee.json","w") as file:
    json.dump(employee,file)

with open("employee.json","r") as file:
    data = json.load(file)

print(data)

text = '{"city":"Chennai"}'

print(json.loads(text))