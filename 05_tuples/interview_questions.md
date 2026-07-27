# Tuples Interview Questions (Questions with Answers)

## 1. What is a tuple?

**Answer:** A tuple is an ordered, immutable collection that allows duplicate values.

---

## 2. Difference between list and tuple?

**Answer:**

- List → Mutable
- Tuple → Immutable

---

## 3. Why is tuple faster than list?

**Answer:** Because tuples are immutable and require less memory management.

---

## 4. What are tuple packing and unpacking?

**Answer:**

Packing:

```python
person = ("Vinoth", 28, "Chennai")
```

Unpacking:

```python
name, age, city = person
```

---

## 5. Can tuples contain lists?

**Answer:** Yes.

```python
data = (10, [20, 30])
```

---

## 6. Can tuples contain duplicate values?

**Answer:** Yes.

---

## 7. Which methods are available for tuples?

**Answer:**

- count()
- index()

---

## 8. Why are tuples used in Data Engineering?

**Answer:** They are useful for storing fixed values such as configuration, coordinates, or database records that should not change.

---

## 9. Can we modify a tuple?

**Answer:** No. Tuples are immutable.

---

## 10. What is the difference between tuple and set?

**Answer:**

| Tuple | Set |
|-------|-----|
| Ordered | Unordered |
| Immutable | Mutable |
| Allows duplicates | Removes duplicates |