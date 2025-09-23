#This program demonstrates the use of attributes in Object Oriented Programming
#Attributes are properties of the class which are used to store data.


#There are two types of attributes in OOP:
#1. Instance Attributes
#2. Class Attributes

'''Instance Attributes:
Instance attributes are defined inside the constructor method using the self keyword and applied for each object of the class which is not unique to all objects of the class.
For example, in the Student class, name, age, and grade are instance attributes because they can have different values for each student object.'''

'''Class Attributes:
Class attributes are defined inside the class but outside any method and are shared among all objects of the class.
For example, in the Student class, college and level are class attributes because they have the same value for all student objects.'''


class Student:
    college = "Kathmandu University"   #Class attribute
    level = "Undergraduate"          #Class attribute
    def __init__(self, name, age):
        self.name = name      #Instance attribute
        self.age = age        #Instance attribute

stu1 = Student("Dipan", 18)   #Creating an object of the class
stu2 = Student("Rimjhim", 19)
stu3 = Student("Sujan", 20)
stu4 = Student("Anusha", 21)

print(stu1.name, stu1.age, stu1.college, stu1.level)   #Accessing the properties of the class using the object
print(stu2.name, stu2.age, stu2.college, stu2.level)
print(stu3.name, stu3.age, stu3.college, stu3.level)
print(stu4.name, stu4.age, stu4.college, stu4.level)
