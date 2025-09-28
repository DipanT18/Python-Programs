#This program is written to demonstrate the use of delete() method in the requests library.

import requests
# Use a test service like httpbin.org to demonstrate DELETE requests
response = requests.delete('https://httpbin.org/delete')
print(f"The status code is: {response.status_code}")