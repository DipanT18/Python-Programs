#Program is written to use the concept of access specifiers in Python

class Car:
    def __init__(self, brand):
        self.__brand = brand  # Private attribute

    def __get_brand(self):
        return self.__brand  # Public method to access private attribute
    
my_car = Car("Toyota")
print(my_car._Car__get_brand())  # Output: Toyota# 

print(my_car.brand) # This will raise an AttributeError because 'brand' is private