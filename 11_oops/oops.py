"""
Topic : Object Oriented Programming

Author : Vinoth Kumar
"""

print("=" * 50)
print("CLASS AND OBJECT")
print("=" * 50)


class Employee:

    company = "OpenAI"

    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.employee_id)
        print(self.name)
        print(self.salary)


emp1 = Employee(101, "Vinoth", 60000)

emp1.display()


print("=" * 50)
print("INHERITANCE")
print("=" * 50)


class Person:

    def speak(self):
        print("Person Speaking")


class Employee(Person):
    pass


emp = Employee()

emp.speak()


print("=" * 50)
print("METHOD OVERRIDING")
print("=" * 50)


class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()

dog.sound()


print("=" * 50)
print("ENCAPSULATION")
print("=" * 50)


class Student:

    def __init__(self):
        self.__marks = 95

    def show_marks(self):
        print(self.__marks)


student = Student()

student.show_marks()


print("=" * 50)
print("CLASS METHOD")
print("=" * 50)


class Company:

    company = "OpenAI"

    @classmethod
    def show_company(cls):
        print(cls.company)


Company.show_company()


print("=" * 50)
print("STATIC METHOD")
print("=" * 50)


class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(10, 20))


print("=" * 50)
print("OOP COMPLETED")
print("=" * 50)