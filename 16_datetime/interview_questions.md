# Datetime Interview Questions (Questions with Answers)

## 1. What is the datetime module?

**Answer:** The `datetime` module provides classes for working with dates and times.

---

## 2. Difference between date and datetime?

**Answer:**

- `date` stores only the date.
- `datetime` stores both date and time.

---

## 3. What is timedelta?

**Answer:** `timedelta` represents the difference between two dates or times and is used to add or subtract time.

---

## 4. What does datetime.now() return?

**Answer:** It returns the current local date and time.

---

## 5. What is strftime()?

**Answer:** It converts a datetime object into a formatted string.

Example:

```python
datetime.now().strftime("%d-%m-%Y")
```

---

## 6. What is strptime()?

**Answer:** It converts a formatted string into a datetime object.

---

## 7. How do you get the current year?

**Answer:**

```python
datetime.now().year
```

---

## 8. What is a timestamp?

**Answer:** A timestamp represents the number of seconds since the Unix epoch (January 1, 1970 UTC).

---

## 9. Why is datetime important in Data Engineering?

**Answer:** It is used for ETL scheduling, log timestamps, partitioning data, audit columns, and report generation.

---

## 10. Which datetime functions are commonly used?

**Answer:**

- datetime.now()
- date.today()
- timedelta()
- strftime()
- strptime()
- timestamp()