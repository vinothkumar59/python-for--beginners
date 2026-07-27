# CSV Interview Questions (Questions with Answers)

## 1. What is a CSV file?

**Answer:** A CSV (Comma-Separated Values) file stores tabular data where each row is a record and values are separated by commas.

---

## 2. What is csv.reader()?

**Answer:** It reads a CSV file row by row and returns each row as a list.

---

## 3. What is csv.writer()?

**Answer:** It writes rows to a CSV file.

---

## 4. What is DictReader()?

**Answer:** It reads a CSV file and returns each row as a dictionary using the column names as keys.

---

## 5. What is DictWriter()?

**Answer:** It writes dictionaries to a CSV file using specified field names.

---

## 6. Why use `newline=""` when writing CSV files?

**Answer:** It prevents extra blank lines from being written, especially on Windows.

---

## 7. When should you use DictReader instead of reader?

**Answer:** Use `DictReader` when you want to access values by column name instead of index.

---

## 8. Why are CSV files important in Data Engineering?

**Answer:** CSV files are widely used for data exchange, ETL pipelines, reporting, and importing/exporting data between systems.

---

## 9. What are the limitations of CSV files?

**Answer:** CSV files do not support data types, nested structures, or metadata, and they can become inefficient for very large datasets.

---

## 10. Which CSV functions are most commonly used?

**Answer:**

- csv.reader()
- csv.writer()
- csv.DictReader()
- csv.DictWriter()