# Dictionary Interview Questions (Questions with Answers)

## 1. What is a dictionary?

**Answer:** A dictionary is a mutable collection of key-value pairs.

---

## 2. Difference between dictionary and list?

**Answer:**

- Dictionary stores key-value pairs.
- List stores indexed values.

---

## 3. Difference between get() and []?

**Answer:**

- get() returns None if key is missing.
- [] raises KeyError.

---

## 4. Difference between keys(), values(), and items()?

**Answer:**

- keys() → returns all keys
- values() → returns all values
- items() → returns key-value pairs

---

## 5. Difference between pop() and popitem()?

**Answer:**

- pop(key) removes a specific key.
- popitem() removes the last inserted key-value pair.

---

## 6. Why are dictionary keys unique?

**Answer:** Each key must uniquely identify a value. Duplicate keys overwrite previous values.

---

## 7. Can dictionary values be duplicated?

**Answer:** Yes.

---

## 8. Can a dictionary contain another dictionary?

**Answer:** Yes. This is called a nested dictionary.

---

## 9. Why are dictionaries heavily used in Data Engineering?

**Answer:** They are ideal for representing JSON data, API responses, configuration settings, and records.

---

## 10. Which dictionary methods are used most in projects?

**Answer:**

- get()
- items()
- keys()
- values()
- update()
- pop()
- copy()
- clear()