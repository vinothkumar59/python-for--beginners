"""
Topic : Lists

Author : Vinoth Kumar
"""

print("=" * 50)
print("LIST")
print("=" * 50)

numbers = [10, 20, 30, 40, 50]

print(numbers)

print("=" * 50)
print("INDEXING")
print("=" * 50)

print(numbers[0])
print(numbers[-1])

print("=" * 50)
print("SLICING")
print("=" * 50)

print(numbers[1:4])

print("=" * 50)
print("APPEND")
print("=" * 50)

numbers.append(60)

print(numbers)

print("=" * 50)
print("EXTEND")
print("=" * 50)

numbers.extend([70, 80])

print(numbers)

print("=" * 50)
print("INSERT")
print("=" * 50)

numbers.insert(0, 5)

print(numbers)

print("=" * 50)
print("REMOVE")
print("=" * 50)

numbers.remove(20)

print(numbers)

print("=" * 50)
print("POP")
print("=" * 50)

numbers.pop()

print(numbers)

print("=" * 50)
print("COUNT")
print("=" * 50)

print(numbers.count(30))

print("=" * 50)
print("INDEX")
print("=" * 50)

print(numbers.index(40))

print("=" * 50)
print("SORT")
print("=" * 50)

numbers.sort()

print(numbers)

print("=" * 50)
print("REVERSE")
print("=" * 50)

numbers.reverse()

print(numbers)

print("=" * 50)
print("COPY")
print("=" * 50)

new_list = numbers.copy()

print(new_list)

print("=" * 50)
print("CLEAR")
print("=" * 50)

sample = [1, 2, 3]

sample.clear()

print(sample)

print("=" * 50)
print("LIST COMPLETED")
print("=" * 50)