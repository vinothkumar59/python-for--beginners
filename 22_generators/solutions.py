def numbers():

    yield 10
    yield 20
    yield 30


generator = numbers()

print(next(generator))

print(next(generator))

print(next(generator))


square = (number ** 2 for number in range(1, 6))

for value in square:
    print(value)


def even():

    for number in range(2, 11, 2):
        yield number


for value in even():
    print(value)