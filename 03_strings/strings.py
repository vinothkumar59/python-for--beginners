"""
Topic : Strings

Author : Vinoth Kumar
"""

print("=" * 50)
print("STRING")
print("=" * 50)

text = "Python Programming"

print(text)

print("=" * 50)
print("INDEXING")
print("=" * 50)

print(text[0])
print(text[-1])

print("=" * 50)
print("SLICING")
print("=" * 50)

print(text[0:6])
print(text[7:])
print(text[::-1])

print("=" * 50)
print("LENGTH")
print("=" * 50)

print(len(text))

print("=" * 50)
print("UPPER LOWER")
print("=" * 50)

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print("=" * 50)
print("REPLACE")
print("=" * 50)

print(text.replace("Python", "Java"))

print("=" * 50)
print("SPLIT")
print("=" * 50)

print(text.split())

print("=" * 50)
print("JOIN")
print("=" * 50)

words = ["Data", "Engineering"]

print(" ".join(words))

print("=" * 50)
print("FIND")
print("=" * 50)

print(text.find("Programming"))

print("=" * 50)
print("COUNT")
print("=" * 50)

print(text.count("m"))

print("=" * 50)
print("STARTS WITH")
print("=" * 50)

print(text.startswith("Python"))

print("=" * 50)
print("ENDS WITH")
print("=" * 50)

print(text.endswith("Programming"))

print("=" * 50)
print("F-STRING")
print("=" * 50)

name = "Vinoth"
age = 28

print(f"My name is {name} and age is {age}")

print("=" * 50)
print("STRING COMPLETED")
print("=" * 50)