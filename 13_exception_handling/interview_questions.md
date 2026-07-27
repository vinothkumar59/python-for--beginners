try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot Divide")

try:
    print(int("ABC"))

except ValueError:
    print("Invalid Number")

try:
    data = [1,2]

    print(data[5])

except IndexError:
    print("Index Error")

try:
    employee = {"name":"Vinoth"}

    print(employee["salary"])

except KeyError:
    print("Key Missing")

try:
    print(100/10)

except:
    print("Error")

else:
    print("Success")

finally:
    print("Completed")