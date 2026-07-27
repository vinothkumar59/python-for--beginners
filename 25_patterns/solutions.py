for i in range(5):
    print("* " * 5)

print()

for i in range(1, 6):
    print("* " * i)

print()

for i in range(5, 0, -1):
    print("* " * i)

print()

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()