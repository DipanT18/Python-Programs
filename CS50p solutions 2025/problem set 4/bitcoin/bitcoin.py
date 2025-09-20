import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    print(f"${float(sys.argv[1])*requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]:,.4f}")
except requests.RequestException:
    pass
except ValueError:
    sys.exit("Command-line argument is not a number")
