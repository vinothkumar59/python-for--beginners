numbers = [10, 20, 30]

print(numbers[0])

print(numbers[-1])

numbers.append(40)

numbers.extend([50, 60])

numbers.insert(0, 5)

numbers.remove(20)

numbers.pop()

numbers.sort()

numbers.reverse()

print(numbers.count(30))

print(numbers.index(30))

copy_list = numbers.copy()

print(copy_list)

copy_list.clear()

print(copy_list)

print(len(numbers))