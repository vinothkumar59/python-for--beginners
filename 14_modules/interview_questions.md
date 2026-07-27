# Modules Interview Questions (Questions with Answers)

## 1. What is a module?

**Answer:** A module is a Python file containing reusable code such as functions, classes, and variables.

---

## 2. What is a package?

**Answer:** A package is a directory containing multiple related Python modules and usually an `__init__.py` file.

---

## 3. Difference between module and package?

**Answer:**

- Module → Single `.py` file.
- Package → Collection of modules.

---

## 4. Difference between `import math` and `from math import sqrt`?

**Answer:**

- `import math` imports the entire module.
- `from math import sqrt` imports only the `sqrt()` function.

---

## 5. What is an alias?

**Answer:** An alias renames a module during import.

Example:

```python
import math as m
```

---

## 6. Why avoid `from module import *`?

**Answer:** It imports everything into the current namespace, making code harder to read and increasing the risk of name conflicts.

---

## 7. What is `__init__.py`?

**Answer:** It marks a directory as a Python package and can contain package initialization code.

---

## 8. Which built-in modules are commonly used in Data Engineering?

**Answer:**

- os
- pathlib
- csv
- json
- logging
- datetime
- math

---

## 9. Why are modules important?

**Answer:** Modules help organize code, improve reusability, and make applications easier to maintain.

---

## 10. How are modules used in ETL projects?

**Answer:** ETL projects separate functionality into modules such as configuration, extraction, transformation, loading, logging, validation, and utility functions.