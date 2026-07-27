from datetime import datetime, timedelta

current = datetime.now()

print(current)

print(current.year)

print(current.month)

print(current.day)

print(current.strftime("%d-%m-%Y"))

text = "01-01-2026"

print(datetime.strptime(text, "%d-%m-%Y"))

print(current + timedelta(days=30))

print(current - timedelta(days=15))

print(current.weekday())

print(current.timestamp())