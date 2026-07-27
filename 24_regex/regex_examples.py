"""
Topic : Regular Expressions

Author : Vinoth Kumar
"""

import re

print("=" * 50)
print("SEARCH")
print("=" * 50)

text = "Python Programming"

result = re.search("Python", text)

print(result.group())

print("=" * 50)
print("MATCH")
print("=" * 50)

result = re.match("Python", text)

print(result.group())

print("=" * 50)
print("FINDALL")
print("=" * 50)

text = "Python SQL PySpark SQL"

print(re.findall("SQL", text))

print("=" * 50)
print("SPLIT")
print("=" * 50)

text = "Python,SQL,PySpark"

print(re.split(",", text))

print("=" * 50)
print("SUB")
print("=" * 50)

text = "Python Programming"

print(re.sub("Python", "Java", text))

print("=" * 50)
print("DIGITS")
print("=" * 50)

text = "Employee 101 Salary 60000"

print(re.findall(r"\d+", text))

print("=" * 50)
print("WORDS")
print("=" * 50)

print(re.findall(r"\w+", text))

print("=" * 50)
print("EMAIL")
print("=" * 50)

email = "vinoth@gmail.com"

pattern = r"\w+@\w+\.\w+"

print(bool(re.fullmatch(pattern, email)))

print("=" * 50)
print("PHONE")
print("=" * 50)

phone = "9876543210"

print(bool(re.fullmatch(r"\d{10}", phone)))

print("=" * 50)
print("REGEX COMPLETED")
print("=" * 50)