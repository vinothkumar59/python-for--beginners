# Logging Interview Questions (Questions with Answers)

## 1. What is logging?

**Answer:** Logging records application events, warnings, errors, and execution details.

---

## 2. Why use logging instead of print()?

**Answer:**

- Logs can be stored in files.
- Different log levels are available.
- Easier debugging in production.
- Better monitoring and auditing.

---

## 3. What are the logging levels?

**Answer:**

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

## 4. What is logging.basicConfig()?

**Answer:** It configures the logging system, including the log file, level, and format.

---

## 5. What does logging.exception() do?

**Answer:** It logs an exception along with the full traceback. It should be used inside an `except` block.

---

## 6. Why are log files important?

**Answer:** They provide a history of application events, making it easier to debug and monitor applications.

---

## 7. What information is usually included in a log?

**Answer:**

- Timestamp
- Log level
- Message
- Exception details (if any)

---

## 8. Which logging level is most commonly used in production?

**Answer:** `INFO` for normal events and `ERROR` for failures. `DEBUG` is mainly used during development.

---

## 9. How is logging used in Data Engineering?

**Answer:** Logging tracks ETL job execution, data validation, file processing, API calls, database operations, and exceptions.

---

## 10. What is the difference between logging.error() and logging.exception()?

**Answer:**

- `logging.error()` logs only the error message.
- `logging.exception()` logs the error message and the complete exception traceback.