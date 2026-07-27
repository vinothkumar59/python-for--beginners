# Lists Interview Questions (Questions with Answers)

## 1. What is a list?

**Answer:** A list is an ordered, mutable collection that allows duplicate values.

---

## 2. Why is a list mutable?

**Answer:** Elements can be added, removed, or modified after creation.

---

## 3. Difference between append() and extend()?

**Answer:**

- append() adds one item.
- extend() adds multiple items from another iterable.

---

## 4. Difference between remove() and pop()?

**Answer:**

- remove() deletes by value.
- pop() deletes by index and returns the removed value.

---

## 5. Difference between sort() and sorted()?

**Answer:**

- sort() modifies the original list.
- sorted() returns a new sorted list.

---

## 6. Difference between copy() and assignment (=)?

**Answer:**

- copy() creates a new list.
- = points to the same list object.

---

## 7. How do you reverse a list?

**Answer:**

```python
numbers.reverse()
```

or

```python
numbers[::-1]
```

---

## 8. How do you find the length of a list?

**Answer:**

```python
len(numbers)
```

---

## 9. Which list methods are commonly used in Data Engineering?

**Answer:**

- append()
- extend()
- sort()
- copy()
- remove()
- pop()

---

## 10. Can a list contain different data types?

**Answer:** Yes.

Example:

```python
data = [10, "Python", 45.5, True]
```