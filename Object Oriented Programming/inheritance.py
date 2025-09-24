#This program is written to demonstrate the use of inheritance in Python
# It shows how a derived class can inherit attributes and methods from a base class
# and how to access private attributes using name mangling.

class Car:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.wheels = 4

class Tesla(Car):
    def __init__(self, start, stop, autopilot, type):
        super().__init__(start, stop)
        self.autopilot = autopilot
        self.type = type

class Model(Tesla):
    def __init__(self, model_name, model_year, model_price, start="Button", stop="Button", autopilot=True, type="Electric"):
        super().__init__(start, stop, autopilot, type)
        self.model_name = model_name
        self.model_year = model_year
        self.model_price = model_price

Car1 = Model("Model X", 2023, 120000)
print(f"Car Name: {Car1.model_name}, Year: {Car1.model_year}, Price: {Car1.model_price}")
print(f"Wheels: {Car1.wheels}")  # Inherited from Car class
print(f"Start: {Car1.start}")  # Inherited from Car class
print(f"Autopilot: {Car1.autopilot}")  # Inherited from Tesla class
print(f"Type: {Car1.type}")  # Inherited from Tesla class
print(f"Stop: {Car1.stop}")  # Inherited from Car class

Car2 = Model("Cybertruck", 2024, 90000)
print(f"Car Name: {Car2.model_name}, Year: {Car2.model_year}, Price: {Car2.model_price}")
print(f"Wheels: {Car2.wheels}")  # Inherited from Car class
print(f"Start: {Car2.start}")  # Inherited from Car class
print(f"Autopilot: {Car2.autopilot}")  # Inherited from Tesla class
print(f"Type: {Car2.type}")  # Inherited from Tesla class
print(f"Stop: {Car2.stop}")  # Inherited from Car class


