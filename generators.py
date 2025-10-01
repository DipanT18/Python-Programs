#This program is written to deminstrate the use of generators in Python.
# Generators are a simple way of creating iterators using functions and the yield statement.

def my_generator():
    for i in range(5000):
        yield i * i  # Yielding the square of the number

# Using the generator
gen = my_generator()
# print(next(gen))  # Output: 0#
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 4
# print(next(gen))  # Output: 9   
# print(next(gen))  # Output: 16


for i in gen:
    print(i)  # This will not print anything as the generator is already exhausted