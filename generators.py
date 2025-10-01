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

# Using normal method
squares = []
for i in range(5000):
    squares.append(i * i)
print(squares)  # This will print the list of squares from 0 to 4999


# The difference is:
# 1. Memory Efficiency: Generators use less memory as they yield items one at a time and do not store the entire list in memory.
# 2. Lazy Evaluation: Generators compute values on the fly and only when requested, making them more efficient for large datasets.
# 3. Simplicity: Generators can be simpler and more readable for certain tasks compared to using lists.
# 4. Performance: For large datasets, generators can be faster as they avoid the overhead of creating and storing a large list in memory.
# 5. Infinite Sequences: Generators can represent infinite sequences, while lists are finite and must fit in memory.
# 6. Iteration: Generators can be iterated only once, while lists can be iterated multiple times.
# # 7. State Retention: Generators retain their state between iterations, while lists do not