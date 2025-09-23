#This is the constructor method used in Object Oriented Programming
#Constructor is a special method which is called when an object of the class is created
#Constructor is used to initialize the properties of the class

class Student: 
    def __init__(self, name, age, grade):   #Constructor method
        self.name = name      #Attributes or properties of the class
        self.age = age
        self.grade = grade

stu1 = Student("Messi", 35, "A")   #Creating an object of the class
stu2 = Student("Neymar", 30, "B")
stu3 = Student("Mbappe", 25, "A+")
stu4 = Student("Ronaldo", 38, "A")
stu5 = Student("Yamal", 20, "A")

print(stu1.name, stu2.name, stu3.name, stu4.name, stu5.name)   #Accessing the properties of the class using the object
print(stu1.age, stu2.age, stu3.age, stu4.age, stu5.age)
print(stu1.grade, stu2.grade, stu3.grade, stu4.grade, stu5.grade)
