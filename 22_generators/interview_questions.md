# Generators Interview Questions (Questions with Answers)

## 1. What is a generator?

**Answer:** A generator is a function that returns values one at a time using the `yield` keyword.

---

## 2. Difference between return and yield?

**Answer:**

- `return` ends the function immediately.
- `yield` pauses the function and resumes from the same point on the next iteration.

---

## 3. Why are generators memory efficient?

**Answer:** They generate values only when needed instead of storing all values in memory.

---

## 4. What is lazy evaluation?

**Answer:** Lazy evaluation means values are produced only when requested.

---

## 5. What is next()?

**Answer:** `next()` retrieves the next value from a generator.

---

## 6. What is a generator expression?

**Answer:**

```python
(number ** 2 for number in range(5))
```

---

## 7. Difference between list comprehension and generator expression?

**Answer:**

- List comprehension creates the entire list in memory.
- Generator expression produces one value at a time.

---

## 8. When should generators be used?

**Answer:** Use generators when processing very large datasets, files, or streams where loading everything into memory is inefficient.

---

## 9. Why are generators useful in Data Engineering?

**Answer:** They help process large files, streaming data, log files, and ETL pipelines efficiently without consuming large amounts of memory.

---

## 10. Which keywords/functions are commonly used with generators?

**Answer:**

- `yield`
- `next()`
- `iter()`
- Generator expressions