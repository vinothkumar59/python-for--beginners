# Dictionaries in Python

## What is a Dictionary?

A dictionary is a mutable collection of key-value pairs.

Example:

```python
employee = {
    "id":101,
    "name":"Vinoth"
}
```

---

## Features

- Mutable
- Key-Value Pair
- Ordered (Python 3.7+)
- Keys are unique
- Values can be duplicated

---

## Common Methods

- get()
- keys()
- values()
- items()
- update()
- pop()
- popitem()
- clear()
- copy()

---

## Best Practices

- Use meaningful keys.
- Prefer get() instead of [] when key may not exist.