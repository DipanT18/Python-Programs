# Odd/Even calculation for a single number
# This is imported program function from math_helper.py
from math_helper import calculate_odd_numbers, calculate_even_numbers

number = int(input("Enter a number to check even/odd: "))

# Check if number is even (function returns non-empty list if true)
if calculate_even_numbers([number]):
    print(f"{number} is even.")
# Check if number is odd (function returns non-empty list if true)
elif calculate_odd_numbers([number]):
    print(f"{number} is odd.")
else:
    print("Unexpected result.")