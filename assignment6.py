# Today
# class and functions basic assignemnet questions in python
# Here are some basic assignment questions on classes and functions in Python:

# Classes:
# Define a class Person with attributes name and age. Create an object of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Lucky", 21)
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")
# Create a class Rectangle with attributes length and width. Include a method to calculate the area of the rectangle.


class Rectangle:
    def area(self, length, width):
        return length*width


area = Rectangle()
print(area.area(10, 5))
# Implement a BankAccount class with methods to deposit and withdraw money. Ensure that the balance does not go negative.


class Bank:
    balance = 0

    def __init__(self, account_number: int):
        self.acc = account_number

    def withdraw(self, amount: int):
        if amount < Bank.balance:
            Bank.balance -= amount
            return f"{amount} Withdrawn. Available balance is {Bank.balance}"
        else:
            return f"Not enough funds. Available balance is {Bank.balance}"

    def deposit(self, amount: int):
        Bank.balance += amount
        return f"Deposit successful. Available balance is {Bank.balance}"


person1 = Bank(1)
print(person1.deposit(1000))
print(person1.withdraw(2000))
print(person1.withdraw(500))
# Design a class Student with attributes name and marks. Include a method that calculates the grade based on marks.


class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def cal_grade(self):
        if self.marks >= 90:
            return "O grade"
        elif self.marks < 90 and self.marks >= 75:
            return "A grade"
        elif self.marks < 75 and self.marks >= 65:
            return "B grade"
        elif self.marks < 65 and self.marks >= 55:
            return "C grade"
        elif self.marks < 55 and self.marks >= 45:
            return "D grade"
        elif self.marks < 45 and self.marks >= 35:
            return "E grade"
        else:
            return "Fail"


student1 = Student("Lucky", 25)
print(student1.cal_grade())
# Write a Vehicle class with a method description() that prints the vehicle type. Create a subclass Car that inherits from Vehicle and overrides the description() method.


class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def description(self):
        if self.wheels == 2:
            return f"{self.name} is a Bike"
        elif self.wheels == 4:
            return f"{self.name} is a car"
        elif self.wheels == 8 or self.wheels == 6:
            return f"{self.name} is a bus"


class Car(Vehicle):
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def description(self):
        return f"{self.model} is a {self.year} car manufactured by {self.name} company"


car = Car("Ford", "Mustang", 1969)
print(car.description())

# Functions:
# Write a function add_numbers(a, b) that returns the sum of two numbers.


def add_numbers(a, b):
    return f"sum of a and b is {a+b}"


print(add_numbers(2, 3))
# Create a function factorial(n) that calculates the factorial of a given number using recursion.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(2))
# Implement a function is_prime(n) that checks if a number is prime.


def is_prime(n):
    if n == 0 or n == 1:
        return "Not Prime"
    if n == 2 or n == 3:
        return "Prime"
    if n % 2 == 0 or n % 3 == 0:
        return "Not Prime"
    i = 5
    while i * i <= n:
        if n % i == 0:
            return "Not Prime"
        i += 6
    return "Prime"


print(is_prime(38))
# Define a function reverse_string(s) that returns the reverse of a given string.


def reverse_string(s):
    return s[::-1]


print(reverse_string("lucky"))

# Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.


def fibonacci(n):
    if n < 1:
        print("Invalid Number of terms")
        return
    prev1 = 1
    prev2 = 0
    print(prev2)
    if n == 1:
        return
    print(prev1)
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        print(curr)


print(fibonacci(10))
