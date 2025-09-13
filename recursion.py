#This code is written to show the simple meaning of recursion in python
#Recursion is a process in which a function calls itself directly or indirectly

def ask_again():
    choice = input("Do you want to run again? (yes/no): ")
    if choice.lower() == "yes":
        ask_again()
    else:
        print("Program ended.")

ask_again()
#In the above code, the function ask_again() calls itself if the user inputs "yes"
#This continues until the user inputs "no", at which point the program ends