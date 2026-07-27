# Strings Interview Questions (Questions with Answers)

## 1. What is a string?

**Answer:** A string is a sequence of characters enclosed in single, double, or triple quotes.

---

## 2. Are strings mutable?

**Answer:** No. Strings are immutable.

---

## 3. Difference between `find()` and `index()`?

**Answer:**
- `find()` returns `-1` if not found.
- `index()` raises `ValueError` if not found.

---

## 4. Difference between `split()` and `join()`?

**Answer:**
- `split()` converts a string into a list.
- `join()` converts a list into a string.

---

## 5. Difference between `upper()` and `capitalize()`?

**Answer:**
- `upper()` converts all characters to uppercase.
- `capitalize()` capitalizes only the first character.

---

## 6. How do you reverse a string?

**Answer:**

```python
text[::-1]
```

---

## 7. How do you count characters?

**Answer:**

```python
text.count("a")
```

---

## 8. How do you replace text?

**Answer:**

```python
text.replace("old", "new")
```

---

## 9. What is an f-string?

**Answer:** An f-string is a formatted string literal introduced in Python 3.6 for embedding expressions directly inside strings.

---

## 10. Which string methods are commonly used in Data Engineering?

**Answer:**

- split()
- strip()
- replace()
- lower()
- upper()
- join()
- startswith()
- endswith()
- find()
- count()