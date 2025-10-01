# This function is written to demonstrate the use of function caching in Python using functools.lru_cache.

import functools
import time

@functools.lru_cache(maxsize=None)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(35)  # Pre-compute some values to populate the cache
fibonacci(35)
fibonacci(35)
fibonacci(35)
    
start_time = time.time()
print(fibonacci(35))  # Output: 9227465

end_time = time.time()
print(f"Time taken with caching: {end_time - start_time} seconds")