# CSV in Python

## What is CSV?

CSV (Comma-Separated Values) is a text file used to store tabular data.

Example:

```csv
id,name,salary
101,Vinoth,60000
102,Rahul,50000
```

---

## csv Module

- csv.reader()
- csv.writer()
- csv.DictReader()
- csv.DictWriter()

---

## Best Practices

- Always use `newline=""`.
- Use `DictReader` when working with column names.
- Use `with open()` for file operations.