# File Handling Interview Questions (Questions with Answers)

## 1. What is file handling?

**Answer:** File handling is the process of creating, reading, writing, appending, and managing files.

---

## 2. Difference between r, w and a?

**Answer:**

- r → Read existing file
- w → Write (overwrites existing content)
- a → Append (adds content to the end)

---

## 3. Why use with open()?

**Answer:** It automatically closes the file, even if an exception occurs.

---

## 4. Difference between read(), readline(), and readlines()?

**Answer:**

- read() → Entire file
- readline() → One line
- readlines() → List of all lines

---

## 5. What is the difference between write() and writelines()?

**Answer:**

- write() writes a single string.
- writelines() writes multiple strings from an iterable.

---

## 6. How do you check if a file exists?

**Answer:**

```python
from pathlib import Path

Path("sample.txt").exists()
```

---

## 7. How do you get a file size?

**Answer:**

```python
Path("sample.txt").stat().st_size
```

---

## 8. What is pathlib?

**Answer:** `pathlib` is a modern Python module for working with files and directories using object-oriented paths.

---

## 9. Why is file handling important in Data Engineering?

**Answer:** ETL pipelines read input files (CSV, JSON, Parquet), transform data, and write output files. File handling is the foundation for these workflows.

---

## 10. Which file modes are most commonly used?

**Answer:**

- r
- w
- a
- r+