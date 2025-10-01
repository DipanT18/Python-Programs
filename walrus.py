# Traditional Method
x = 10
if x > 5:
    print(x)

# Using Walrus Operator
if (x := 10) > 5:
    print(x)



# Traditional Method
User_input = input("Enter a message (or 'quit'): ")
while User_input != 'quit':
    print(f"You entered: {User_input}")
    User_input = input("Enter a message (or 'quit'): ")

# Using Walrus Operator
while (User_input := input("Enter a message (or 'quit'): ")) != 'quit':
    print(f"You entered: {User_input}")
