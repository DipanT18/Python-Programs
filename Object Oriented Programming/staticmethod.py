#This program is written to demonstrate the use of static method in OOPs
# Static method is a method which is used to directly call and operate the method without using instance or self keyword.


class Operate:

    @staticmethod
    def add(a,b):
        return a + b
    
result1 = Operate.add(5,6)
result2 = Operate.add("Dipan"," Timalsina")
print(result1)
print(result2)