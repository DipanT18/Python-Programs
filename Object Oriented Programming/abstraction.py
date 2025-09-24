#This program is written to demonstrate the use of abstraction in Object Oriented Programming
#Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object

class BankAccount:
    __total_cash = 0  # Private class attribute

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
        BankAccount.__total_cash += balance  # Add initial balance to total cash
       

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            BankAccount.__total_cash += amount  # Update total cash
            return f"Deposited: {amount}. New Balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            BankAccount.__total_cash -= amount  # Update total cash
            return f"Withdrew: {amount}. New Balance: {self.__balance}"
        else:
            return "Insufficient balance or invalid withdrawal amount."

    def get_balance(self):
        return f"Current Balance: {self.__balance}"

    # (Optional) For admin use only, not shown to users
    @classmethod
    def _get_total_cash(cls):
        return cls.__total_cash
# The account number and balance are hidden from direct access
# Users can interact with the account only through the deposit, withdraw, and get_balance methods

account1 = BankAccount("123456789", 1000)
print(f"Account Number: {account1._BankAccount__account_number}")  # Accessing private attribute using name mangling
print(account1.deposit(500))        # Deposited: 500. New Balance: 1500
print(account1.withdraw(200))       # Withdrew: 200. New Balance: 1300
print(account1.get_balance())       # Current Balance: 1300

account2 = BankAccount("987654321", 2000)
print(f"Account Number: {account2._BankAccount__account_number}")  # Accessing private attribute using name mangling
print(account2.deposit(1000))       # Deposited: 1000. New Balance: 3000
print(account2.withdraw(5000))      # Insufficient balance or invalid withdrawal amount.
print(account2.get_balance())       # Current Balance: 3000

account3 = BankAccount("555555555", 500)
print(f"Account Number: {account3._BankAccount__account_number}")  # Accessing private attribute using name mangling
print(account3.deposit(-100))       # Deposit amount must be positive.
print(account3.withdraw(100))       # Withdrew: 100. New Balance: 400
print(account3.get_balance())       # Current Balance: 400

# Trying to access private attributes directly will raise an AttributeError
# print(account1.__balance)  # Uncommenting this line will cause an error