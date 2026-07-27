from functools import reduce

square = lambda x: x * x

print(square(10))

add = lambda a, b: a + b

print(add(5, 10))

numbers = [1, 2, 3]

print(list(map(lambda x: x * 2, numbers)))

print(list(filter(lambda x: x > 1, numbers)))

print(reduce(lambda x, y: x + y, numbers))