"""
Topic : Datetime

Author : Vinoth Kumar
"""

from datetime import datetime, date, time, timedelta

print("=" * 50)
print("CURRENT DATE & TIME")
print("=" * 50)

current = datetime.now()

print(current)

print("=" * 50)
print("TODAY")
print("=" * 50)

print(date.today())

print("=" * 50)
print("DATE")
print("=" * 50)

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)

print("=" * 50)
print("TIME")
print("=" * 50)

current_time = datetime.now().time()

print(current_time)

print("=" * 50)
print("FORMAT DATE")
print("=" * 50)

print(current.strftime("%d-%m-%Y"))
print(current.strftime("%d/%m/%Y"))
print(current.strftime("%H:%M:%S"))
print(current.strftime("%A"))
print(current.strftime("%B"))

print("=" * 50)
print("PARSE DATE")
print("=" * 50)

text = "27-07-2026"

parsed = datetime.strptime(text, "%d-%m-%Y")

print(parsed)

print("=" * 50)
print("TIMEDELTA")
print("=" * 50)

future = current + timedelta(days=10)

past = current - timedelta(days=10)

print(future)
print(past)

print("=" * 50)
print("WEEKDAY")
print("=" * 50)

print(current.weekday())

print("=" * 50)
print("TIMESTAMP")
print("=" * 50)

print(current.timestamp())

print("=" * 50)
print("DATETIME COMPLETED")
print("=" * 50)