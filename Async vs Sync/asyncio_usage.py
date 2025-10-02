#Today is Dashain. So, happy Dashain to all the Nepali's out there.

#Let's move to the code now.
#this program is written to demonstrate the use of asyncronous programming in python using asyncio module.

import asyncio
import time

async def make_coffee():
    print("Starting to make coffee...")
    print("Grinding coffee beans...")
    await asyncio.sleep(2)  # Simulating time taken to grind beans
    print("Boiling water...")
    await asyncio.sleep(3)  # Simulating time taken to boil water
    print("Brewing coffee...")
    await asyncio.sleep(3)  # Simulating time taken to brew coffee
    print("Coffee is ready!")

async def make_toast():
    print("Starting to make toast...")
    print("Putting bread in toaster...")
    await asyncio.sleep(2)  # Simulating time taken to toast bread
    print("Taking out toast...")
    await asyncio.sleep(1)  # Simulating time taken to take out toast
    print("Spreading butter and jam...")
    await asyncio.sleep(3)  # Simulating time taken to spread butter and jam
    print("Toast is ready!")

async def make_breakfast_async():
    """Asynchronous breakfast - FAST!"""
    print("\n✅ ASYNCHRONOUS BREAKFAST (With Asyncio)")
    print("-" * 40)
    start = time.time()
    
    # Run all tasks concurrently!
    results = await asyncio.gather(
        make_coffee(),
        make_toast()
    )
    end = time.time()
    print(f"\nBreakfast is ready! (Time taken: {end - start:.2f} seconds)")
    print("-" * 40)
    return results

# Run the async function
if __name__ == "__main__":
    asyncio.run(make_breakfast_async())

