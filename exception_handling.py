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
        return
    finally:
        print("Execution completed.")
    print("Thank you for using the division program.")

divide_numbers()
#In the above code, we handle two types of exceptions: ZeroDivisionError and ValueError
#The else block executes if no exceptions are raised, and the finally block always executes

#See here for comparison between finally and print statement
#The finally block will execute regardless of whether the function is returned or an exception is raised
#The print statement after the finally block will only execute if the function does not return early