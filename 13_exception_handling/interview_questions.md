# Exception Handling Interview Questions (Questions with Answers)

## 1. What is an exception?

**Answer:** An exception is a runtime error that interrupts the normal execution of a program.

---

## 2. What is the purpose of try?

**Answer:** The `try` block contains code that might raise an exception.

---

## 3. What is except?

**Answer:** It catches and handles exceptions raised in the `try` block.

---

## 4. What is else?

**Answer:** The `else` block runs only if no exception occurs.

---

## 5. What is finally?

**Answer:** The `finally` block always executes, whether an exception occurs or not.

---

## 6. What is raise?

**Answer:** `raise` is used to create and throw an exception manually.

---

## 7. Difference between Exception and BaseException?

**Answer:** `Exception` is the base class for most application errors. `BaseException` is the root of Python's exception hierarchy and also includes system-level exceptions like `KeyboardInterrupt` and `SystemExit`.

---

## 8. Why should we catch specific exceptions?

**Answer:** It makes debugging easier and avoids hiding unexpected errors.

---

## 9. Why is exception handling important in ETL?

**Answer:** ETL jobs process many files and records. Exception handling prevents a single bad record or missing file from crashing the entire pipeline and allows logging and recovery.

---

## 10. Which exceptions are commonly used in Python?

**Answer:**

- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError