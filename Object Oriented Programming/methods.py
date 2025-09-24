#This program is written to demonstrate the use of methods in Object Oriented Programming

#Methods are functions defined inside a class that operate on the data contained within the class and its objects.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is starting."

    def stop_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is stopping."

    def display_info(self):
        return f"Car Info: {self.year} {self.make} {self.model}"

Car1 = Car("Toyota", "Fortuner", 2020)
Car2 = Car("Hyundai", "Creta", 2022)
Car3 = Car("Mercedes", "G-wagon", 2021)
Car4 = Car("BMW", "X5", 2023)
print(Car1.start_engine())
print(Car2.stop_engine())
print(Car3.display_info())
print(Car4.start_engine())