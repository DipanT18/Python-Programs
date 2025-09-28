#This program is written to demonstrate the use of raise_for_status() method in the requests library.
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://httpbin.org/status/404')
    # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")  # e.g. 404 Not Found