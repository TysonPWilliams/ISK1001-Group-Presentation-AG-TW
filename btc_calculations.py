import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import csv
import secret
from colors import *

def get_btc_price():
    """
    Fetches the current BTC price from CoinMarketCap API.
    """

    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": "BTC",
        "convert": "AUD"
    }
    headers = {
        "X-CMC_PRO_API_KEY": secret.API_KEY # Replace with your CoinMarketCap API key
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status() # Raise an exception for non-2xx status codes
        data = response.json()
        btc_price = data['data']['BTC'][0]['quote']['AUD']['price']
        return btc_price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f'An error occured while fetching BTC price: {e}')
        raise

def read_csv_data(filename):
    """Reads the CSV file and extracts the user's BTC holdings."""
    btc_holdings = 0.0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        for row in reader:
            try:
                btc_holdings += float(row[0])
            except IndexError:
                print(f"{error_text}Error: 'crypto.csv' does not contain any added BTC yet{constants.RESET}")
                input(f'{primary_text}----Press Enter to Continue----{constants.RESET}')
    return btc_holdings

def calculate_aud_value(btc_price, btc_holdings):
    """Calculates the total AUD value of the user's BTC holdings."""
    aud_value = btc_price * btc_holdings
    return aud_value