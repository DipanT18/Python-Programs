#This program is written to demonstrate the use of class methods in Python
# It shows how to define and use class methods to manipulate class-level data.

class Student:
    school_name = "Harvard Business School"  # Class variable

    def __init__(self, school_name):
        self.school_name = school_name  # Instance variable

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name  # Modify class variable

# Creating instances of Student
student1 = Student("Stanford University")
print(student1.school_name)  # Output: Stanford University