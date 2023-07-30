"""Day4 Monday 26th June 2023

Object Oriented Programming (OOP)

Classes - blueprint for creating objects
"""

"""
1. inheritence
2. polymorphism
3. abstraction
"""


class Car:
    """A class that represents a car."""

    def _init_(self, car_make, car_model, car_year):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
    def start_engine(self):
        """Starts the car's engine."""
        print("Engine has started")

    def stop_engine(self):
        """Stops the car's engine."""
        print("Engine has stopped")


#my_car = Car("Toyota", "Model", 2000)
"""Model
print(my_car.car_model)
print(my_car.car_make)
print(my_car.car_year)
print(my_car.start_engine())
print(my_car.stop_engine())
"""
print("------------------------------------------------------------------")


# Simple Program to show student details
class Student:
    """classs to show student details"""

    def _init_(self, name, regno):
        self.name = name
        self.regno = regno
def display(self):
        """moethod to display student details"""
        print("Student name is: ", self.name)
        print("Student registration number is:", self.regno)


student_obj = Student("Bryan", "21/U/0663")
student_obj.display()
print("----------------------------------------------------------")


# Exercise
# Calculate the area and circumference of a circle


class AreaCircum:
    """program to calculate area and circumference of a circle"""

    def _init_(self, radius, pie):
        self.radius = radius
        self.pie = pie
