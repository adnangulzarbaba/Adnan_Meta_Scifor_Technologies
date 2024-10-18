"""
Python Basics

1. What are Python data types?
"""

# Integer, Float, String, List, Tuple, Dictionary, Set
x = 14               # Integer
y = 0.14             # Float
name = "Barry"       # String
fruits = ["apple", "banana", "cherry"]  # List
coordinates = (36, 53)                  # Tuple
person = {"name": "Berry", "age": 23}    # Dictionary
unique_numbers = {1, 2, 3}              # Set

"""Explain the difference between list, tuple, and set."""

lst = [1, 2, 3]  # Mutable, ordered, allows duplicates
tup = (1, 2, 3)  # Immutable, ordered, allows duplicates
s = {1, 2, 3}    # Mutable, unordered, unique elements

"""3. How do you handle exceptions in Python?"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero error!")
else:
    print("No errors occurred.")
finally:
    print("Code execution completed.")

"""4. What are Python decorators?"""

def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

"""5. What is a lambda function?"""

square = lambda x: x * x
print(square(4))  # Output: 16

"""6. How does Python handle multithreading?"""

import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Wait for thread to finish

"""7. How do you work with files in Python?"""

with open("example.txt", "w") as f:
    f.write("Hello, World!")

with open("example.txt", "r") as f:
    content = f.read()
    print(content)

"""OOP Implementation

1. What is Object-Oriented Programming (OOP)?
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

dog = Dog("Roger", 5)
dog.bark()  # Output: Roger barks!

"""2. What is a class and an object in Python?"""

# Class as a blueprint
class Car:
    def __init__(self, model, year):
        self.model = model  # Attribute
        self.year = year    # Attribute

    def display_info(self):  # Method
        print(f"Car: {self.model}, Year: {self.year}")

# Creating objects (instances) of the class
car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2018)

# Accessing attributes and methods of the objects
car1.display_info()  # Output: Car: Toyota, Year: 2020
car2.display_info()  # Output: Car: Honda, Year: 2018

"""3. How do you create a class in Python?"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the class
person1 = Person("Barry", 23)
person1.greet()  # Output: Hello, my name is Barry and I am 25 years old.

"""4. What are instance variables and class variables?"""

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

"""5. What is the purpose of the __init__ method?"""

class MyClass:
    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method called")

"""6. What are self and cls?"""

class MyClass:
    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method called")

"""7. What is inheritance?"""

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()  # Output: Bark

"""8. Explain method overriding and method overloading."""

class Parent:
    def say_hello(self):
        print("Hello from parent")

class Child(Parent):
    def say_hello(self):
        print("Hello from child")

child = Child()
child.say_hello()  # Output: Hello from child

"""9. What is multiple inheritance? How does Python handle it?"""

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()  # Output: A (Method Resolution Order)

"""10. What are abstract classes and interfaces in Python?"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

"""11. What is polymorphism in Python?"""

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.sound()

"""12. What is encapsulation in OOP?"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

"""13. What are getters and setters in Python?"""

class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

"""14. How do you implement operator overloading in Python?"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2  # Uses __add__ method

"""15. What is a static method and a class method in Python?"""

class MyClass:
    @staticmethod
    def static_method():
        print("Static method called")

    @classmethod
    def class_method(cls):
        print("Class method called")