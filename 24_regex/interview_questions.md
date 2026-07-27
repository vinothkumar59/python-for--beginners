# Regex Interview Questions (Questions with Answers)

## 1. What is Regex?

**Answer:** Regex (Regular Expression) is a sequence of characters used to search, match, validate, and manipulate text.

---

## 2. Which module is used for Regex in Python?

**Answer:**

```python
import re
```

---

## 3. Difference between search() and match()?

**Answer:**

- `search()` looks for the pattern anywhere in the string.
- `match()` checks only at the beginning of the string.

---

## 4. What does findall() do?

**Answer:** It returns a list of all matches found in the string.

---

## 5. What does sub() do?

**Answer:** It replaces matching text with another string.

---

## 6. What does split() do?

**Answer:** It splits a string using a regex pattern.

---

## 7. What is a raw string (`r""`)?

**Answer:** A raw string treats backslashes literally, making regex patterns easier to write.

Example:

```python
r"\d+"
```

---

## 8. Which regex patterns are commonly used?

**Answer:**

- `\d` → Digit
- `\w` → Word character
- `\s` → Whitespace
- `^` → Start of string
- `$` → End of string
- `.` → Any character

---

## 9. Why is Regex important in Data Engineering?

**Answer:** Regex is used for data validation, log parsing, extracting values, cleaning text, validating emails and phone numbers, and processing files in ETL pipelines.

---

## 10. Which Regex functions are most commonly used?

**Answer:**

- `search()`
- `match()`
- `findall()`
- `finditer()`
- `sub()`
- `split()`