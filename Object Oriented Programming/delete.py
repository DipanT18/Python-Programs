#This is a simple program to demonstrate the concept of deleting an object in Python using the del keyword

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} belongs to {self.breed} breed and says Woof!"
    
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())  # Output: Buddy belongs to Golden Retriever breed and says
# Woof!

# Deleting the dog1 object
del dog1.name
del dog1.breed
del dog1