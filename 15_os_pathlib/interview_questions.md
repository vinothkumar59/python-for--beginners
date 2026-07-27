# OS & Pathlib Interview Questions (Questions with Answers)

## 1. What is the os module?

**Answer:** The `os` module provides functions for interacting with the operating system, such as working with directories, files, and environment variables.

---

## 2. What is pathlib?

**Answer:** `pathlib` is an object-oriented module for handling file system paths.

---

## 3. Difference between os and pathlib?

**Answer:**

- `os` uses functions.
- `pathlib` uses objects and methods, making code more readable.

---

## 4. How do you get the current working directory?

**Answer:**

```python
os.getcwd()
```

---

## 5. How do you create a directory?

**Answer:**

```python
Path("demo").mkdir()
```

or

```python
os.mkdir("demo")
```

---

## 6. How do you check if a file exists?

**Answer:**

```python
Path("sample.txt").exists()
```

---

## 7. How do you delete a file?

**Answer:**

```python
Path("sample.txt").unlink()
```

---

## 8. How do you delete an empty directory?

**Answer:**

```python
Path("demo").rmdir()
```

---

## 9. Why is pathlib preferred in modern Python?

**Answer:** It provides a cleaner, object-oriented API for working with paths and is cross-platform.

---

## 10. How are os and pathlib used in Data Engineering?

**Answer:** They are used to manage input/output folders, locate files, create directories for ETL jobs, move files, validate file existence, and automate file-based workflows.