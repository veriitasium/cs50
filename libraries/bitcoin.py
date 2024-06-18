# pip3 install requests

import requests
import sys

try:
    quantity = int(sys.argv[1])

    request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    json_response = request.json()

    amount = float(json_response['bpi']['USD']['rate'].replace(',', '')) * quantity

    print(f"${amount:,.4f}")

except IndexError:
    print("Missing command-line argument")
# except ValueError:
#     print("Command-line argument is not a number")
except requests.RequestException:
    print("error...")