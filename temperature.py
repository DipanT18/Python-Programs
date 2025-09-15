#This code is written to show the use of f sring in python
#f string is used to format the string in python
#f string is used to embed expressions inside string literals, using curly braces {}

temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = (temperature * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
#The above code converts the temperature from celsius to fahrenheit
#The :.2f is used to format the float to 2 decimal places
#The °F is used to denote the temperature in fahrenheit
#The f before the string is used to denote that it is an f string
