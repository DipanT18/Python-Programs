#This program is written to demonstrate the use of request module to send HTTP GET request to retrieve data 

import requests

response = requests.get('https://www.google.com')

if 'application/json' in response.headers.get('content-type', ''):
    print(response.json())
else:
    print("Response is not JSON. Content type:", response.headers.get('content-type'))
    print("First 10000 characters:")
    print(response.text[:10000])