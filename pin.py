#this program is to classify a pin code as valid or invalid
#Here we will use while loop and if-else statements

pin1 = 899001

pin = int(input("Enter your pin code: "))
while True:
    if pin == pin1:
        print("Valid pin code")
        break
    else:
        print("Invalid pin code")
        pin = int(input("Re-enter your pin code: "))