"""
Topic : File Handling

Author : Vinoth Kumar
"""

print("=" * 50)
print("WRITE")
print("=" * 50)

with open("sample.txt", "w") as file:
    file.write("Welcome to Python\n")
    file.write("File Handling Example\n")

print("File Created")

print("=" * 50)
print("READ")
print("=" * 50)

with open("sample.txt", "r") as file:
    print(file.read())

print("=" * 50)
print("READLINE")
print("=" * 50)

with open("sample.txt", "r") as file:
    print(file.readline())

print("=" * 50)
print("READLINES")
print("=" * 50)

with open("sample.txt", "r") as file:
    print(file.readlines())

print("=" * 50)
print("APPEND")
print("=" * 50)

with open("sample.txt", "a") as file:
    file.write("Data Engineering\n")

print("Data Added")

print("=" * 50)
print("READ AFTER APPEND")
print("=" * 50)

with open("sample.txt", "r") as file:
    print(file.read())

print("=" * 50)
print("ITERATE FILE")
print("=" * 50)

with open("sample.txt", "r") as file:

    for line in file:
        print(line.strip())

print("=" * 50)
print("FILE EXISTS")
print("=" * 50)

from pathlib import Path

path = Path("sample.txt")

print(path.exists())

print("=" * 50)
print("FILE SIZE")
print("=" * 50)

print(path.stat().st_size, "Bytes")

print("=" * 50)
print("FILE HANDLING COMPLETED")
print("=" * 50)