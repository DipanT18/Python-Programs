#Here I will show you the use cases of dir() method, help() method and __dict__ attributes in python

class Student:
    def __init__(self, faculty, rank, pass_condition):
        self.faculty = faculty
        self.rank = rank
        self.pass_condition = pass_condition

s1 = Student("Engineering", "1", "True")
print(s1.rank, s1.faculty, s1.pass_condition)

#dir() method --> It is used to return a list of all the attributes and methods available for the object.

print (dir(s1))

#help() method --> It is used to get the documentation for an object, class or anything including description of its attributes and methods

print (help(Student))

#__dict__ attribute --> It is used to return a dictionairy representation of an object's attributes. It is a useful tool for introspection.

print(s1.__dict__)