"""
Topic : Sets

Author : Vinoth Kumar
"""

print("=" * 50)
print("SET")
print("=" * 50)

numbers = {10,20,30,40,50}

print(numbers)

print("=" * 50)
print("ADD")
print("=" * 50)

numbers.add(60)

print(numbers)

print("=" * 50)
print("UPDATE")
print("=" * 50)

numbers.update([70,80])

print(numbers)

print("=" * 50)
print("REMOVE")
print("=" * 50)

numbers.remove(20)

print(numbers)

print("=" * 50)
print("DISCARD")
print("=" * 50)

numbers.discard(100)

print(numbers)

print("=" * 50)
print("POP")
print("=" * 50)

value = numbers.pop()

print(value)

print(numbers)

print("=" * 50)
print("COPY")
print("=" * 50)

new_set = numbers.copy()

print(new_set)

print("=" * 50)
print("CLEAR")
print("=" * 50)

sample = {1,2,3}

sample.clear()

print(sample)

print("=" * 50)
print("UNION")
print("=" * 50)

a = {1,2,3}

b = {3,4,5}

print(a.union(b))

print("=" * 50)
print("INTERSECTION")
print("=" * 50)

print(a.intersection(b))

print("=" * 50)
print("DIFFERENCE")
print("=" * 50)

print(a.difference(b))

print("=" * 50)
print("SYMMETRIC DIFFERENCE")
print("=" * 50)

print(a.symmetric_difference(b))

print("=" * 50)
print("MEMBERSHIP")
print("=" * 50)

print(2 in a)

print(10 in a)

print("=" * 50)
print("ITERATION")
print("=" * 50)

for value in a:
    print(value)

print("=" * 50)
print("SET COMPLETED")
print("=" * 50)