#This program is written to demonstrate the use of enumerate function in python

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
for index, fruit in enumerate(fruits, start=1):
    print(f"{index} {fruit}")


#This program gives the numbering of the elements in a list