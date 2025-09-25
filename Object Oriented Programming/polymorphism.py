#This program is written to demonstrate polymorphism in Python
# It shows how different classes can have methods with the same name but behave differently.

class Complex:
    def  __init__ (self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "+", self.img, "i")

    def __add__(self, other):
        newreal = self.real + other.real
        newimg = self.img + other.img
        return Complex(newreal, newimg)
    
    def __sub__(self, other):
        newreal = self.real - other.real
        newimg = self.img - other.img
        return Complex(newreal, newimg)
    
    def __mul__(self, other):
        newreal = self.real * other.real - self.img * other.img
        newimg = self.real * other.img + self.img * other.real
        return Complex(newreal, newimg)


num1 = Complex(3, 4)
num1.show()  # Output: 3 + 4 i

num2 = Complex(5, 6)
num2.show()  # Output: 5 + 6 i

num3 = num1 + num2
num3.show()  # Output: 8 + 10 i

num4 = num1 - num2
num4.show()  # Output: -2 + -2 i

num5 = num1 * num2
num5.show()  # Output: -9 + 38 i





