#This program is used to demonstrate the concept of private attributes and methods in Object Oriented Programming
#Private attributes and methods are those that cannot be accessed directly from outside the class

class LinkedIn_Account:
    def __init__(self, username, password):
        self.username = username  # Public attribute
        self.__password = password  # Private attribute


    def get_password(self):  # Private method
        return self.__password
    
acc1 = LinkedIn_Account("user1", "pass123")
print(f"Username: {acc1.username}")  # Accessing public attribute
print(f"Password: {acc1.__password}")  # Trying to access private attribute directly will raise an AttributeError
print(f"Password: {acc1.get_password()}")  # Accessing private attribute via public method
