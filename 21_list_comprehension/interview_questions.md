# List Comprehension Interview Questions (Questions with Answers)

## 1. What is list comprehension?

**Answer:** List comprehension is a concise way to create a new list using a single expression.

---

## 2. What is the syntax of list comprehension?

**Answer:**

```python
[expression for item in iterable]
```

---

## 3. How do you filter values in a list comprehension?

**Answer:**

```python
[number for number in numbers if number % 2 == 0]
```

---

## 4. Can you use if-else inside a list comprehension?

**Answer:** Yes.

Example:

```python
["Even" if number % 2 == 0 else "Odd" for number in numbers]
```

---

## 5. Why is list comprehension faster than a for loop?

**Answer:** It is optimized internally by Python and produces more concise code.

---

## 6. Can list comprehensions contain nested loops?

**Answer:** Yes.

Example:

```python
[(x, y) for x in [1, 2] for y in [3, 4]]
```

---

## 7. When should you avoid list comprehension?

**Answer:** Avoid it when the logic becomes too complex or difficult to read.

---

## 8. Why is list comprehension useful in Data Engineering?

**Answer:** It is useful for filtering, transforming, cleaning, and preparing datasets efficiently.

---

## 9. Does list comprehension modify the original list?

**Answer:** No. It creates a new list.

---

## 10. Difference between a for loop and list comprehension?

**Answer:**

- `for` loop is more flexible for complex logic.
- List comprehension is shorter and ideal for simple transformations.