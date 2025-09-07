import requests

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies=usd"
    try:
        response = requests.get(url).json()
        return response[coin.lower()]["usd"]
    except KeyError:
        print(f"Could not fetch price for {coin}. Setting price to 0.")
        return 0
    except requests.exceptions.RequestException:
        print("Error connecting to CoinGecko. Setting price to 0.")
        return 0
