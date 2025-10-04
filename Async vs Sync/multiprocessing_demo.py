#This program is written to demonstrate the use of multiprocessing in python.

import multiprocessing
import time

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

def make_breakfast_multiprocessing():
    """Multiprocessing breakfast - FAST!"""
    print("\n✅ MULTIPROCESSING BREAKFAST")
    print("-" * 40)
    start = time.time()
    
    # Create processes for each task
    coffee_process = multiprocessing.Process(target=make_coffee)
    toast_process = multiprocessing.Process(target=make_toast)
    
    # Start the processes
    coffee_process.start()
    toast_process.start()
    
    # Wait for both processes to complete
    coffee_process.join()
    toast_process.join()
    
    end = time.time()
    print(f"\nBreakfast is ready! (Time taken: {end - start:.2f} seconds)")
    print("-" * 40)

    # Note: On Windows, the 'if __name__ == "__main__":' guard is necessary for multiprocessing to work correctly.
if __name__ == "__main__":
    make_breakfast_multiprocessing()