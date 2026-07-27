# Lambda Interview Questions (Questions with Answers)

## 1. What is a lambda function?

**Answer:** A lambda function is an anonymous function written in a single line using the `lambda` keyword.

---

## 2. Difference between lambda and normal function?

**Answer:**

- Lambda → Anonymous, single expression.
- Normal function → Uses `def` and can contain multiple statements.

---

## 3. What is map()?

**Answer:** `map()` applies a function to every item in an iterable.

---

## 4. What is filter()?

**Answer:** `filter()` returns elements that satisfy a condition.

---

## 5. What is reduce()?

**Answer:** `reduce()` repeatedly applies a function to reduce an iterable to a single value. It is available in the `functools` module.

---

## 6. Why use lambda with sorted()?

**Answer:** It allows custom sorting based on a specific key.

Example:

```python
sorted(data, key=lambda x: x[1])
```

---

## 7. Can lambda contain multiple statements?

**Answer:** No. A lambda function can contain only one expression.

---

## 8. Where are lambda functions used in Data Engineering?

**Answer:** Lambda functions are commonly used for sorting, filtering, transformations, and quick operations on collections of data.

---

## 9. Is lambda faster than a normal function?

**Answer:** No. Lambda functions are mainly used for concise code, not for performance improvements.

---

## 10. Which functions are commonly used with lambda?

**Answer:**

- map()
- filter()
- reduce()
- sorted()
- max()
- min()