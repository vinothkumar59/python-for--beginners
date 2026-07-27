class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


emp = Employee("Vinoth")

emp.display()


class Person:

    def speak(self):
        print("Hello")


class Student(Person):
    pass


student = Student()

student.speak()


class Math:

    @staticmethod
    def square(n):
        return n * n


print(Math.square(5))