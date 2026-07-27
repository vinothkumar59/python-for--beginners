# Decorators Interview Questions (Questions with Answers)

## 1. What is a decorator?

**Answer:** A decorator is a function that adds or modifies the behavior of another function without changing its source code.

---

## 2. Why are decorators used?

**Answer:**

- Code reuse
- Logging
- Authentication
- Validation
- Performance monitoring

---

## 3. What does the @ symbol do?

**Answer:** It applies a decorator to a function.

Example:

```python
@decorator
def hello():
    pass
```

---

## 4. What is a wrapper function?

**Answer:** A wrapper function executes additional code before or after calling the original function.

---

## 5. Why use *args and **kwargs in decorators?

**Answer:** They allow decorators to work with functions that accept any number of positional or keyword arguments.

---

## 6. What is functools.wraps()?

**Answer:** It preserves the original function's metadata, such as its name and docstring, after decoration.

---

## 7. Can multiple decorators be applied to one function?

**Answer:** Yes.

Example:

```python
@decorator1
@decorator2
def function():
    pass
```

---

## 8. Where are decorators used in Data Engineering?

**Answer:** Decorators are used for logging, measuring execution time, validating input, retry logic, and access control in ETL pipelines and data services.

---

## 9. What happens when a decorated function is called?

**Answer:** The decorator's wrapper function executes, optionally adding behavior before and/or after the original function.

---

## 10. Which modules commonly use decorators?

**Answer:**

- Flask
- FastAPI
- Airflow
- Django
- Pytest