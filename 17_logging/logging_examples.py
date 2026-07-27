"""
Topic : Logging

Author : Vinoth Kumar
"""

import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

print("=" * 50)
print("LOGGING")
print("=" * 50)

logging.debug("Debug Message")

logging.info("Application Started")

logging.warning("Low Disk Space")

logging.error("Database Connection Failed")

logging.critical("Application Crashed")

print("Log Messages Written")

print("=" * 50)
print("TRY EXCEPT LOGGING")
print("=" * 50)

try:
    print(10 / 0)

except ZeroDivisionError as error:
    logging.exception(error)

print("Exception Logged")

print("=" * 50)
print("CUSTOM LOG")
print("=" * 50)

employee = "Vinoth"

logging.info(f"Employee : {employee}")

salary = 60000

logging.info(f"Salary : {salary}")

print("Employee Logged")

print("=" * 50)
print("LOGGING COMPLETED")
print("=" * 50)