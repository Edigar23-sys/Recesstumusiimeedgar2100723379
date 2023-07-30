#object oriented programming 
#classes 
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age]

    class 
        """
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("Starting engine")

    def stop_engine(self):
        print("Stopping engine")

    def drive(self):
        print("Driving")

    my_Car = Car("Toyota", "Corolla", 2022)
    print(my_Car.make)
    print(my_Car.model)
    print(my_Car.year)
    my_Car.start_engine()
    my_Car.stop_engine()

"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return self.length + self.width
                
my_rectangle = Rectangle(15,5)
print(my_rectangle.calculate_area())
print(my_rectangle.length)
print(my_rectangle.width)
print(my_rectangle.calculate_perimeter())

class Student:
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def display_details(self):
        print("Name", self.name, "year", self.year, "course", self.course)

Edgar = Student("Tumusiime", "Software Engineer", 3)
Edgar.display_details()
