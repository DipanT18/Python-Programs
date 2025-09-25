#This program is written to demonstrate the use of property decorators in Python
# It shows how to define and use properties to manage attribute access in a class.

class Marks:
    def __init__(self, phy, che, math):
        self._phy = phy 
        self._che = che  
        self._math = math  
        
    @property
    def Percentage(self):
        return str((self._phy + self._che + self._math) / 3) + "%"
    
# Creating an instance of Marks
student1 = Marks(90, 80, 70)
print(student1.Percentage)  # Output: 80.0%

student1._phy = 96  # Modifying the private attribute directly
student1._che = 90  # Modifying the private attribute directly
student1._math = 79  # Modifying the private attribute directly

print(student1.Percentage)  # Output: 88.33333333333333%