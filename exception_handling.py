#This program is written to demonstrate exception handling in Python

def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

divide_numbers()
#In the above code, we handle two types of exceptions: ZeroDivisionError and ValueError
#The else block executes if no exceptions are raised, and the finally block always executes