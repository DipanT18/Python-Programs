#Circle normal ans simple operations

'''class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def diameter(self):
        return 2 * self.radius
    
cir1 = Circle(5)
print("Area:", cir1.area())  # Output: Area: 78.53975
print("Circumference:", cir1.circumference())  # Output: Circumference: 31.4159
print("Diameter:", cir1.diameter())  # Output: Diameter: 10
cir2 = Circle(10)
print("Area:", cir2.area())  # Output: Area: 314.159
print("Circumference:", cir2.circumference())  # Output: Circum
print("Diameter:", cir2.diameter())  # Output: Diameter: 20'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def diameter(self):
        return 2 * self.radius
    
cir1 = Circle(int(input("Enter radius of circle 1: ")))
print("Area:", cir1.area())  
print("Circumference:", cir1.circumference())  
print("Diameter:", cir1.diameter())  
cir2 = Circle(int(input("Enter radius of circle 2: ")))
print("Area:", cir2.area())  
print("Circumference:", cir2.circumference()) 
print("Diameter:", cir2.diameter())