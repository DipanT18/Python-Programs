#Here are some basics of arithmetic calculations wrapped in seperate functions.
import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_square_area(side):
    return side**2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

def calculate_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    # Circle area
    radius = float(input("Enter the radius of the circle: "))
    area_of_circle = calculate_circle_area(radius)
    print(f"Area of circle: {area_of_circle}")

    # Square area
    side = float(input("Enter the side length of the square: "))
    area_of_square = calculate_square_area(side)
    print(f"Area of square: {area_of_square}")

    # Rectangle area
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area_of_rectangle = calculate_rectangle_area(length, breadth)
    print(f"Area of rectangle: {area_of_rectangle}")

    # Odd/Even calculation for a list of numbers
    numbers = input("Enter numbers separated by spaces for odd/even calculation: ")
    numbers_list = [int(num) for num in numbers.split()]
    odd_numbers = calculate_odd_numbers(numbers_list)
    even_numbers = calculate_even_numbers(numbers_list)
    print(f"Odd numbers: {odd_numbers}")
    print(f"Even numbers: {even_numbers}")

# This ensures the main() function only runs when the script is executed directly,
# not when it's imported as a module
if __name__ == "__main__":
    main()