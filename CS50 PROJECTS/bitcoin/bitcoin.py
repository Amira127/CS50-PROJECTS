import requests
import sys

try:
    bitcoin = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    coin = o["bpi"]["USD"]["rate_float"]
    amount = coin * bitcoin
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()
except ValueError:
    sys.exit("Command-line argument is not a number")
except:
    sys.exit("Missing command-line argument")
