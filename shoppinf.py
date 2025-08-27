def available_items():
    return [
        "phone charger", "power bank", "t-Shirt", "Cargo pants", "Economics Book",
        "Iphone 13 pro", "Samsung S23 Ultra", "beard trimmer", "camera", "Titan watch"
    ]

def prices():
    return {
        "phone charger": 100,
        "power bank": 150,
        "t-Shirt": 220,
        "Cargo pants": 325,
        "Economics Book": 830,
        "Iphone 13 pro": 935,
        "Samsung S23 Ultra": 1040,
        "beard trimmer": 145,
        "camera": 650,
        "Titan watch": 555
    }
    

def add_to_cart(cart, item):
    if item in available_items():
        cart.append(item)
        return True
    return False

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item in cart:
            print("- " + item)

def remove_from_cart(cart, item):
    if item in cart:
        cart.remove(item)
        return True
    return False

def calculate_bill(cart):
    total = 0
    for item in cart:
        total += prices().get(item, 0)
    return total

available_items_list = available_items()
print("Available items:")
for item in available_items_list:
    print("- " + item)
check = input("Do you want to check prices? (yes/no)")
if check == "yes":
    price_dict = prices()
    print("\nPrices:")
    for item, price in price_dict.items():
        print(f"- {item}: {price}")
else:
    print("Okay, no prices will be shown.")
    print("Thank you for visiting our store!")
    exit()
check1= input("Do you want to add items to cart? (yes/no)")
if check1 == "yes":
    cart = []
    while True:
        item = input("Enter the item to add to cart (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        if add_to_cart(cart, item):
            print(f"{item} has been added to your cart.")
        else:
            print(f"{item} is not available.")
    view_cart(cart)
    remove = input("Do you want to remove any item from the cart? (yes/no): ").strip().lower()
    if remove == "yes":
        item_to_remove = input("Enter the item to remove: ").strip()
        if remove_from_cart(cart, item_to_remove):
            print(f"{item_to_remove} has been removed from your cart.")
        else:
            print(f"{item_to_remove} is not in your cart.")
    view_cart(cart)
    total_bill = input("Would you mind calculating total bill now? (yes/no): ").strip().lower()
    if total_bill == "yes":
        total_bill = calculate_bill(cart)
        print(f"Your total bill is: {total_bill}")
        print("Thank you for shopping with us!")
    else:
        print("Okay, items added to cart are removed.")
        cart.clear()
        print("Your cart is now empty.")
        view_cart(cart)
elif check1 == "no":
    print("Okay, no items will be added to the cart.")
    print("Thank you for visiting our store!")
    exit()
else:
    print("Invalid option. Please try again.")
    exit()