#This program is written to show the usage of time module in python


import time

current_time = time.time()
print(f"The time since unix epoch is: {current_time} ") #----> Purpose: Returns current time as seconds since Unix epoch (January 1, 1970)

#Time formatting ---> It is the process of converting a datetime object into a custom string representation, using special format codes to specify how each part of the date and time should be displayed.
formatted = time.strftime("%Y-%m-%d %H:%M:%S") 
print(f"The time is: {formatted}")

#Time parsing ----> Purpose: Parses string to time tuple according to format
parsed = time.strptime("2023-09-19", "%Y-%m-%d")
print(f"The parsed time is: {parsed}")

#Local time ----> Purpose: Converts seconds since epoch to local time tuple
local_time = time.localtime()
print(local_time)

#time.perf_counter()
# Purpose: Returns high-resolution timer for measuring elapsed time
start = time.perf_counter()
for i in range(1000):
    print(i)
elapsed = time.perf_counter() - start

print(f"\nLoop completed in {elapsed:.6f} seconds")



#Timesleep is the method of taking break between executing codes
print("Hey guys, I am Dipan")
time.sleep(4)
print("I am gonna be engineer.")
time.sleep(3)
print("And")
time.sleep(3)
print("Innovative Businessman")



