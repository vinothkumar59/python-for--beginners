def greet():
    print("Hello")

greet()

def add(a,b):
    return a+b

print(add(10,20))

def square(n):
    return n*n

print(square(5))

def maximum(a,b):
    return max(a,b)

print(maximum(100,50))

def total(*numbers):
    return sum(numbers)

print(total(10,20,30))

def employee(**data):

    for key,value in data.items():
        print(key,value)

employee(name="Vinoth",city="Chennai")