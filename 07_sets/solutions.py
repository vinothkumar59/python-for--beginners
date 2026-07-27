numbers = {10,20,30}

numbers.add(40)

numbers.update([50,60])

numbers.remove(20)

numbers.discard(100)

numbers.pop()

copy_set = numbers.copy()

print(copy_set)

copy_set.clear()

print(copy_set)

a = {1,2,3}

b = {3,4,5}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))

print(2 in a)

for value in a:
    print(value)

data = [1,2,2,3,3,4]

print(set(data))