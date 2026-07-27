# File Handling in Python

## What is File Handling?

File handling allows Python programs to create, read, write, append, and manage files.

---

## File Modes

- r  → Read
- w  → Write
- a  → Append
- x  → Create
- r+ → Read & Write

---

## Common Methods

- open()
- read()
- readline()
- readlines()
- write()
- writelines()
- close()

---

## Best Practice

Always use:

```python
with open() as file:
```

It automatically closes the file.