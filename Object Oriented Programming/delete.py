#This is a simple program to demonstrate the concept of deleting an object in Python using the del keyword

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} belongs to {self.breed} breed and says Woof!"
    
# Creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")

# Deleting the dog1 object
del dog.name
del dog.breed
del dog

#Printing the object after deletion will raise an error
print(dog.bark())  # This will raise a NameError since dog has been deleted