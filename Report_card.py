#This is a report card generation program using Object Oriented Programming concepts
#This program will take student details and their marks in various subjects as input and generate a report card

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total() / len(self.marks)

    def generate_report_card(self):
        print(f"Report Card for {self.name} (Roll No: {self.roll_number})")
        print("-" * 40)
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        total = self.calculate_total()
        average = self.calculate_average()
        print("-" * 40)
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print("-" * 40)
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Grade: {grade}")
if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    student = Student(name, roll_number)

    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            mark = float(input(f"Enter marks for {subject}: "))
            if 0 <= mark <= 100:
                student.add_marks(subject, mark)
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for marks.")

    student.generate_report_card()