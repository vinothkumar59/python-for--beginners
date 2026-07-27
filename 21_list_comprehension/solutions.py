numbers = [1, 2, 3, 4, 5]

print([number ** 2 for number in numbers])

print([number ** 3 for number in numbers])

print([number for number in numbers if number % 2 == 0])

print([number for number in numbers if number % 2 != 0])

names = ["python", "sql"]

print([name.upper() for name in names])

print([len(name) for name in names])

print(["Even" if number % 2 == 0 else "Odd" for number in numbers])