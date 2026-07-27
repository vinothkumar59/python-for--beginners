# Sets Interview Questions (Questions with Answers)

## 1. What is a set?

**Answer:** A set is an unordered, mutable collection of unique values.

---

## 2. Does a set allow duplicate values?

**Answer:** No. Duplicate values are automatically removed.

---

## 3. Difference between remove() and discard()?

**Answer:**

- remove() raises KeyError if the value does not exist.
- discard() does nothing if the value does not exist.

---

## 4. Difference between union() and intersection()?

**Answer:**

- union() returns all unique elements.
- intersection() returns only common elements.

---

## 5. What is difference()?

**Answer:** Returns elements present in the first set but not in the second.

---

## 6. What is symmetric_difference()?

**Answer:** Returns elements that exist in either set but not in both.

---

## 7. Why are sets unordered?

**Answer:** Sets are implemented for fast membership testing, not ordered storage.

---

## 8. Why are sets useful in Data Engineering?

**Answer:** They are commonly used to remove duplicates, compare datasets, and perform set operations efficiently.

---

## 9. Can a set contain another set?

**Answer:** No. Sets can only contain hashable (immutable) elements. You can use a `frozenset` if needed.

---

## 10. Which set methods are commonly used?

**Answer:**

- add()
- update()
- remove()
- discard()
- union()
- intersection()
- difference()
- symmetric_difference()
- clear()