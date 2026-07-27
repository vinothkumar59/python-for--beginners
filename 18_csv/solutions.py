import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id","name","marks"])

    writer.writerow([1,"A",90])

    writer.writerow([2,"B",95])

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("students.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])