#This program is written to get the name and marks of 3 subjects of a student and calculate the average marks using OOP concepts

class Student: 
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def average(self):
        return (self.math + self.science + self.english) / 3

student1 = Student("Manjil", 85, 90, 95)
print(f"The average marks of {student1.name} is {student1.average()}")

student2 = Student("Sujal", 80, 70, 75)
print(f"The average marks of {student2.name} is {student2.average()}")

student3 = Student("Anish", 60, 65, 70)
print(f"The average marks of {student3.name} is {student3.average()}")

student4 = Student("Aarav", 95, 100, 90)
print(f"The average marks of {student4.name} is {student4.average()}")