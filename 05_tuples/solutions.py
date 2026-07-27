numbers = (10, 20, 30, 40)

print(numbers[0])

print(numbers[-1])

print(numbers[1:3])

print(numbers.count(20))

print(numbers.index(30))

print(len(numbers))

employee = (
    101,
    "Vinoth",
    ("Python", "SQL")
)

print(employee)

person = ("Vinoth", 28, "Chennai")

name, age, city = person

print(name)
print(age)
print(city)

for item in numbers:
    print(item)

print(20 in numbers)