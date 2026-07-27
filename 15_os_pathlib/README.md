# OS & Pathlib in Python

## What is os?

The `os` module provides functions to interact with the operating system.

---

## What is pathlib?

`pathlib` is a modern module for working with file and directory paths.

---

## Common os Functions

- getcwd()
- chdir()
- mkdir()
- listdir()
- remove()
- rename()

---

## Common pathlib Methods

- exists()
- mkdir()
- unlink()
- stat()
- is_file()
- is_dir()

---

## Best Practices

- Prefer `pathlib` over `os.path` for new projects.
- Always check if a file exists before deleting it.