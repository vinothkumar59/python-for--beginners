from pathlib import Path

with open("demo.txt", "w") as file:
    file.write("Python\n")
    file.write("SQL\n")

with open("demo.txt", "r") as file:
    print(file.read())

with open("demo.txt", "a") as file:
    file.write("PySpark\n")

with open("demo.txt", "r") as file:
    print(file.readlines())

path = Path("demo.txt")

print(path.exists())

print(path.stat().st_size)