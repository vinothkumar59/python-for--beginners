"""
Topic : CSV

Author : Vinoth Kumar
"""

import csv

print("=" * 50)
print("WRITE CSV")
print("=" * 50)

with open("employees.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id","name","department","salary"])

    writer.writerow([101,"Vinoth","Data Engineering",60000])

    writer.writerow([102,"Rahul","Python",50000])

print("CSV Created")

print("=" * 50)
print("READ CSV")
print("=" * 50)

with open("employees.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

print("=" * 50)
print("DICT READER")
print("=" * 50)

with open("employees.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)

print("=" * 50)
print("DICT WRITER")
print("=" * 50)

with open("employees_dict.csv","w",newline="") as file:

    fieldnames = ["id","name","city"]

    writer = csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "id":1,
        "name":"Vinoth",
        "city":"Chennai"
    })

print("Dictionary CSV Created")

print("=" * 50)
print("FILTER DATA")
print("=" * 50)

with open("employees.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        if int(row["salary"]) >= 55000:
            print(row)

print("=" * 50)
print("CSV COMPLETED")
print("=" * 50)