# Decorators in Python

## What is a Decorator?

A decorator is a function that modifies or extends the behavior of another function without changing its source code.

Example:

```python
@decorator
def greet():
    print("Hello")
```

---

## Benefits

- Code Reusability
- Logging
- Authentication
- Timing Functions
- Validation

---

## Best Practices

- Keep decorators simple.
- Use functools.wraps() for production code.