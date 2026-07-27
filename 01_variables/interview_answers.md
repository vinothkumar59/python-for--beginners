# Variables - Interview Answers

## 1. What is a variable?

### Answer

A variable is a name that refers to an object stored in memory. It allows us to store and access data during program execution.

Example:

```python
name = "Vinoth"
age = 28
```

---

## 2. Why do we use variables?

### Answer

Variables are used to:

- Store data
- Reuse values
- Make code readable
- Avoid hardcoding values

---

## 3. What are variable naming rules?

### Answer

- Must start with a letter or underscore (_)
- Cannot start with a number
- Cannot contain spaces
- Cannot use Python keywords
- Variable names are case-sensitive

Example:

```python
employee_name = "Rahul"
_employee = 10
salary = 50000
```

Invalid:

```python
2employee = "Rahul"
employee-name = "Rahul"
class = "Python"
```

---

## 4. Is Python case-sensitive?

### Answer

Yes.

```python
age = 25
Age = 30

print(age)
print(Age)
```

These are two different variables.

---

## 5. What is dynamic typing?

### Answer

Python determines the data type automatically.

Example:

```python
x = 10
x = "Python"
```

The same variable can refer to different types during execution.

---

## 6. What is multiple assignment?

### Answer

Assigning the same value to multiple variables.

```python
x = y = z = 100
```

---

## 7. How do you assign multiple variables in one line?

### Answer

```python
name, age, city = "Vinoth", 28, "Chennai"
```

---

## 8. How do you swap two variables?

### Answer

```python
a = 10
b = 20

a, b = b, a
```

No temporary variable is required.

---

## 9. What does type() do?

### Answer

It returns the data type of an object.

Example:

```python
print(type(10))
print(type("Python"))
```

---

## 10. What does id() do?

### Answer

It returns the memory identity of an object.

Example:

```python
x = 10

print(id(x))
```

---

## 11. Difference between = and ==

### Answer

`=` is the assignment operator.

`==` is the comparison operator.

Example:

```python
x = 10

print(x == 10)
```

---

## 12. Difference between local and global variables?

### Answer

Global variables are declared outside a function and can be accessed throughout the program.

Local variables are declared inside a function and exist only within that function.

---

## 13. What is variable scope?

### Answer

Variable scope defines where a variable can be accessed.

Types:

- Global Scope
- Local Scope

---

## 14. What does del do?

### Answer

The `del` keyword removes a variable reference.

```python
x = 100

del x
```

---

## 15. What happens if you access a deleted variable?

### Answer

Python raises a `NameError`.

Example:

```python
x = 10

del x

print(x)
```

---

## 16. What are Python keywords?

### Answer

Keywords are reserved words that have predefined meanings.

Examples:

```python
if
else
class
for
while
def
return
```

---

## 17. Can a variable change its type?

### Answer

Yes.

Python is dynamically typed.

Example:

```python
x = 10

x = "Hello"
```

---

## 18. What are mutable and immutable objects?

### Answer

Mutable:

- list
- dict
- set

Immutable:

- int
- float
- tuple
- string

---

## 19. Explain Python memory management.

### Answer

Python stores objects in memory and variables reference those objects. Memory is automatically managed by Python's garbage collector.

---

## 20. What is the best practice for naming variables?

### Answer

- Use meaningful names.
- Follow `snake_case`.
- Avoid single-letter names except in loops.
- Use constants in uppercase.

Example:

```python
employee_salary = 50000

MAX_SIZE = 100
```