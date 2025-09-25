#Using inheritance to create a base class and derived classes

from os import name


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Engineer(Employee):
    def __init__(self, faculty, specialty):
        self.faculty = faculty
        self.specialty = specialty
        super().__init__(name, id)

    def display(self):
        super().display()
        print(f"Faculty: {self.faculty}, Specialty: {self.specialty}")

eng1 = Engineer("Engineering", "Software")
eng1.display()
