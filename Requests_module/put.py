#This program is written to demonstrate the use of delete() method in the requests library.
import requests
import json

# Example of a PUT request
data = {'name': 'Dipan', 'age': 24}
response = requests.put('https://httpbin.org/put', json = data)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response Body:", response.json())