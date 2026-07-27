# JSON Interview Questions (Questions with Answers)

## 1. What is JSON?

**Answer:** JSON (JavaScript Object Notation) is a lightweight data-interchange format used for storing and exchanging structured data.

---

## 2. Difference between JSON and Python dictionary?

**Answer:**

- JSON is a text format.
- A Python dictionary is an in-memory object.

---

## 3. Difference between dump() and dumps()?

**Answer:**

- `dump()` writes JSON to a file.
- `dumps()` converts a Python object to a JSON string.

---

## 4. Difference between load() and loads()?

**Answer:**

- `load()` reads JSON from a file.
- `loads()` converts a JSON string into a Python object.

---

## 5. Why is JSON used in APIs?

**Answer:** JSON is lightweight, human-readable, and supported by almost every programming language, making it ideal for data exchange.

---

## 6. Can JSON store nested objects?

**Answer:** Yes. JSON supports nested objects and arrays.

---

## 7. What Python data types map to JSON?

**Answer:**

- dict → object
- list → array
- str → string
- int/float → number
- bool → true/false
- None → null

---

## 8. Why is JSON important in Data Engineering?

**Answer:** JSON is commonly used for REST APIs, configuration files, cloud services, NoSQL databases, and ETL pipelines.

---

## 9. How do you pretty-print JSON?

**Answer:**

```python
json.dumps(data, indent=4)
```

---

## 10. Which JSON functions are most commonly used?

**Answer:**

- json.load()
- json.loads()
- json.dump()
- json.dumps()