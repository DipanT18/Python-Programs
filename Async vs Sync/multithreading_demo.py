# This program demonstrate the use and meaning of multithreading in python.
import threading
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
    
def make_breakfast_multithreaded():
    """Multithreaded breakfast - FAST!"""
    print("\n✅ MULTITHREADED BREAKFAST")
    print("-" * 40)
    start = time.time()
    
    # Create threads for each task
    coffee_thread = threading.Thread(target=make_coffee)
    toast_thread = threading.Thread(target=make_toast)
    
    # Start the threads
    coffee_thread.start()
    toast_thread.start()
    
    # Wait for both threads to complete
    coffee_thread.join()
    toast_thread.join()
    
    end = time.time()
    print(f"\nBreakfast is ready! (Time taken: {end - start:.2f} seconds)")
    print("-" * 40)

# Run the multithreaded function
if __name__ == "__main__":
    make_breakfast_multithreaded()#Today is Dashain. So, happy Dashain to all the Nepali's out there.