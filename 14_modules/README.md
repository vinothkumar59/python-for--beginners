# Modules and Packages in Python

## What is a Module?

A module is a Python file containing functions, classes, or variables that can be imported into another program.

Example:

```python
import math
```

---

## What is a Package?

A package is a collection of related Python modules.

Example:

```
package/
    __init__.py
    math_utils.py
    string_utils.py
```

---

## Import Types

- import module
- from module import function
- import module as alias
- from module import *

---

## Common Built-in Modules

- math
- random
- os
- pathlib
- datetime
- csv
- json
- logging

---

## Best Practices

- Import only what you need.
- Avoid using `from module import *`.