"""
Topic : Modules

Author : Vinoth Kumar
"""

import math
import random
import os
from pathlib import Path
from datetime import datetime

print("=" * 50)
print("MATH MODULE")
print("=" * 50)

print(math.sqrt(25))
print(math.pow(2, 5))
print(math.ceil(10.2))
print(math.floor(10.9))

print("=" * 50)
print("RANDOM MODULE")
print("=" * 50)

print(random.randint(1, 100))
print(random.choice(["Python", "SQL", "PySpark"]))

print("=" * 50)
print("OS MODULE")
print("=" * 50)

print(os.getcwd())

print("=" * 50)
print("PATHLIB MODULE")
print("=" * 50)

path = Path("sample.txt")

print(path.exists())

print("=" * 50)
print("DATETIME MODULE")
print("=" * 50)

print(datetime.now())

print("=" * 50)
print("ALIAS")
print("=" * 50)

import math as m

print(m.factorial(5))

print("=" * 50)
print("IMPORT FUNCTION")
print("=" * 50)

from math import pi

print(pi)

print("=" * 50)
print("MODULES COMPLETED")
print("=" * 50)