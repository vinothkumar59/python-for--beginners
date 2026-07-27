from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper


@decorator
def hello():

    print("Hello")


hello()


def log(function):

    @wraps(function)
    def wrapper(*args):

        print("Started")

        result = function(*args)

        print("Completed")

        return result

    return wrapper


@log
def square(number):

    return number * number


print(square(5))