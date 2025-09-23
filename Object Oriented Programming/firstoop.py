#This is the first program in OOP
#OOP means mapping real world objects to code


class Employee:   #Class is a blueprint of an object
    name = "Ronaldo"      #Attributes or properties of the class
    age = 36
    salary = 100000

emp1 = Employee()   #Creating an object of the class
#Object is an instance of a class
#Object contains all the properties and methods of the class and it is the real world entity which performs actions

print(emp1.name)   #Accessing the properties of the class using the object
print(emp1.age)    
print(emp1.salary)

#We can also print location of the object in memory
print(emp1)   #<__main__.Employee object at 0x000001BA2B3C4D0>
#Here 0x000001BA2B3C4D0 is the location of the object in memory
