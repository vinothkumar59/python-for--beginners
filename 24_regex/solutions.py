import re

print(re.search("Python", "Python SQL").group())

print(re.match("Python", "Python SQL").group())

print(re.findall(r"\d+", "Age 28 Salary 60000"))

print(re.findall(r"\w+", "Python SQL"))

print(re.sub("SQL", "PySpark", "Python SQL"))

print(re.split(",", "A,B,C"))

print(bool(re.fullmatch(r"\d{6}", "600001")))

print(bool(re.fullmatch(r"\d{10}", "9876543210")))