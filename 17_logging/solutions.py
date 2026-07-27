import logging

logging.basicConfig(
    filename="demo.log",
    level=logging.INFO,
    format="%(levelname)s : %(message)s"
)

logging.info("Application Started")

logging.warning("Warning Message")

logging.error("Error Message")

try:
    print(10/0)

except ZeroDivisionError as error:
    logging.exception(error)

logging.info("Completed")