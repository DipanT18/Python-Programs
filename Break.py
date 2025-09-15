#this is the simulation of do while loop in python
#which is also called break statement

number = int(input("Enter a number: "))
while True:
    if number == 0:
        print("Zero")
        break
    elif number % 2 == 0:
        print("Even number")
        number = int(input("Re-enter a number: "))
    else:
        print("Odd number")
        number = int(input("Re-enter a number: "))