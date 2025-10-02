#This program is written to demostrate the use of non-asyncronous programming in python.
#This is to show and clear cut the difference between asyncronous and non-asyncronous programming.

import time
from tracemalloc import start

def make_coffee():
    print("Starting to make coffee...")
    print("Grinding coffee beans...")
    time.sleep(2)  # Simulating time taken to grind beans
    print("Boiling water...")
    time.sleep(3)  # Simulating time taken to boil water
    print("Brewing coffee...")
    time.sleep(3)  # Simulating time taken to brew coffee
    print("Coffee is ready!")

def make_toast():
    print("Starting to make toast...")
    print("Putting bread in toaster...")
    time.sleep(2)  # Simulating time taken to toast bread
    print("Taking out toast...")
    time.sleep(1)  # Simulating time taken to take out toast
    print("Spreading butter and jam...")
    time.sleep(3)  # Simulating time taken to spread butter and jam
    print("Toast is ready!")

def make_breakfast_sync():
    """Synchronous breakfast - SLOW!"""
    print("\n❌ SYNCHRONOUS BREAKFAST (Without Asyncio)")
    print("-" * 40)
    start = time.time()
    
    # Run tasks one after the other
    make_coffee()
    make_toast()
    
    end = time.time()
    print(f"\nBreakfast is ready! (Time taken: {end - start:.2f} seconds)")
    print("-" * 40)

# Call the function
make_breakfast_sync()