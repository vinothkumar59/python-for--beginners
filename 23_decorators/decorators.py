"""
Topic : Decorators

Author : Vinoth Kumar
"""

from functools import wraps

print("=" * 50)
print("SIMPLE DECORATOR")
print("=" * 50)


def decorator(function):

    @wraps(function)
    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


@decorator
def greet():

    print("Welcome to Python")


greet()

print("=" * 50)
print("DECORATOR WITH ARGUMENTS")
print("=" * 50)


def log(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Function Started")

        result = function(*args, **kwargs)

        print("Function Completed")

        return result

    return wrapper


@log
def add(a, b):

    return a + b


print(add(10, 20))

print("=" * 50)
print("MULTIPLE DECORATORS")
print("=" * 50)


def uppercase(function):

    @wraps(function)
    def wrapper():

        return function().upper()

    return wrapper


def stars(function):

    @wraps(function)
    def wrapper():

        return "***** " + function() + " *****"

    return wrapper


@stars
@uppercase
def message():

    return "python"


print(message())

print("=" * 50)
print("DECORATORS COMPLETED")
print("=" * 50)