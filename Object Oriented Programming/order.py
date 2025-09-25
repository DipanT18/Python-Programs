class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __compare_price__(self, other_order):
        if self.price > other_order.price:
            return f"{self.item} > {other_order.item}"
        elif self.price < other_order.price:
            return f"{self.item} < {other_order.item}"
        else:
            return f"{self.item} = {other_order.item}"
        
    def __gt__(self, order2):
        return self.price > order2.price
        
order1 = Order("Laptop", 120000)
order2 = Order("Smartphone", 80000)

print(order1.__compare_price__(order2))  # Output: Laptop > Smartphone





# print(order2 < order1)  # Output: True
# # Note: The last line will raise an error because the '<' operator is not defined for the Order class.

print(order1 > order2)  # Output: True

# print(order1 == order2)  # Output: False
# # Note: The last three lines will raise errors because the '>', '<', and '=='

