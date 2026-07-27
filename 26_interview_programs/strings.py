"""
Topic : String Interview Programs

Author : Vinoth Kumar
"""

print("=" * 60)
print("STRING INTERVIEW PROGRAMS")
print("=" * 60)

# ----------------------------------------------------
# 1 Reverse String
# ----------------------------------------------------

print("\n1. Reverse String")

text = "Python"

print(text[::-1])

# ----------------------------------------------------
# 2 Palindrome String
# ----------------------------------------------------

print("\n2. Palindrome String")

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ----------------------------------------------------
# 3 Count Vowels
# ----------------------------------------------------

print("\n3. Count Vowels")

text = "Python Programming"

count = 0

for char in text.lower():

    if char in "aeiou":
        count += 1

print(count)

# ----------------------------------------------------
# 4 Count Words
# ----------------------------------------------------

print("\n4. Count Words")

text = "Python SQL PySpark"

print(len(text.split()))

# ----------------------------------------------------
# 5 Count Characters
# ----------------------------------------------------

print("\n5. Count Characters")

text = "Python"

print(len(text))

# ----------------------------------------------------
# 6 Remove Spaces
# ----------------------------------------------------

print("\n6. Remove Spaces")

text = "Python Programming"

print(text.replace(" ", ""))

# ----------------------------------------------------
# 7 Count Uppercase Letters
# ----------------------------------------------------

print("\n7. Count Uppercase")

text = "PyTHon"

count = 0

for char in text:

    if char.isupper():
        count += 1

print(count)

# ----------------------------------------------------
# 8 Count Lowercase Letters
# ----------------------------------------------------

print("\n8. Count Lowercase")

text = "PyTHon"

count = 0

for char in text:

    if char.islower():
        count += 1

print(count)

# ----------------------------------------------------
# 9 Character Frequency
# ----------------------------------------------------

print("\n9. Character Frequency")

text = "programming"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

# ----------------------------------------------------
# 10 Anagram
# ----------------------------------------------------

print("\n10. Anagram")

first = "listen"
second = "silent"

if sorted(first) == sorted(second):
    print("Anagram")
else:
    print("Not Anagram")

print("\n" + "=" * 60)
print("STRING PROGRAMS COMPLETED")
print("=" * 60)