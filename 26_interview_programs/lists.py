"""
Topic : List Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("LIST INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Find Maximum
# ----------------------------------------------------

print("\n1. Find Maximum")

numbers = [10, 45, 23, 89, 12]

print(max(numbers))

# ----------------------------------------------------
# 2 Find Minimum
# ----------------------------------------------------

print("\n2. Find Minimum")

print(min(numbers))

# ----------------------------------------------------
# 3 Second Largest Number
# ----------------------------------------------------

print("\n3. Second Largest Number")

unique = list(set(numbers))

unique.sort()

print(unique[-2])

# ----------------------------------------------------
# 4 Remove Duplicates
# ----------------------------------------------------

print("\n4. Remove Duplicates")

numbers = [10, 20, 20, 30, 40, 40, 50]

print(list(set(numbers)))

# ----------------------------------------------------
# 5 Sum of List
# ----------------------------------------------------

print("\n5. Sum of List")

numbers = [10, 20, 30, 40]

print(sum(numbers))

# ----------------------------------------------------
# 6 Average of List
# ----------------------------------------------------

print("\n6. Average of List")

print(sum(numbers) / len(numbers))

# ----------------------------------------------------
# 7 Merge Two Lists
# ----------------------------------------------------

print("\n7. Merge Two Lists")

list1 = [1, 2, 3]

list2 = [4, 5, 6]

print(list1 + list2)

# ----------------------------------------------------
# 8 Linear Search
# ----------------------------------------------------

print("\n8. Linear Search")

numbers = [10, 20, 30, 40, 50]

search = 30

if search in numbers:
    print("Found")
else:
    print("Not Found")

# ----------------------------------------------------
# 9 Bubble Sort
# ----------------------------------------------------

print("\n9. Bubble Sort")

numbers = [5, 3, 8, 2, 1]

for i in range(len(numbers)):

    for j in range(len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:

            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

# ----------------------------------------------------
# 10 Selection Sort
# ----------------------------------------------------

print("\n10. Selection Sort")

numbers = [64, 25, 12, 22, 11]

for i in range(len(numbers)):

    minimum = i

    for j in range(i + 1, len(numbers)):

        if numbers[j] < numbers[minimum]:

            minimum = j

    numbers[i], numbers[minimum] = numbers[minimum], numbers[i]

print(numbers)

print("\n" + "=" * 60)
print("LIST PROGRAMS COMPLETED")
print("=" * 60)