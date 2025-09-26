#This program demonstrate the use of method overriding in OOPs
#Method overriding means it allows you to redefine the method into a child class

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        # 1. The super() call must be inside the __init__ method.
        # 2. Call the parent constructor with the arguments it expects (x and y).
        super().__init__(radius, radius)
        
        # 3. Initialize the attribute specific to the Circle class.
        self.radius = radius
    
    def area(self):
        return (22/7)* super().area()

Rect = Shape(4, 8)
Area_of_rect = Rect.area()
print(f"The area is: {Area_of_rect}")

circ = Circle(5)
Area_of_Circle = circ.area()
print(f"The area of circle is: {Area_of_Circle}")

