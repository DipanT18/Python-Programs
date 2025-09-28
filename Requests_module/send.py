import requests

# Use a test service like httpbin.org to demonstrate POST requests
data = {'username': 'John', 'password': 'Secret'}
response = requests.post('https://httpbin.org/post', data=data)

# Check the status of the code
print(f"The status code is: {response.status_code}")

# Check if the request was successful
if response.ok:
    print("Response Content (JSON):")
    try:
        # httpbin.org returns valid JSON, so this will succeed
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        # This block will no longer be executed
        print(response.text)
else:
    print("Request failed with an error.")

        