# Importing the requests library to make HTTP requests to the CoinMarketCap API
import requests

# Importing specific excepttions from requests to handle errors like connection issues, timeouts and excessive redirects
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# Importing the csv module to read and write CSV files
import csv

# Importing the secret.py module we created, which contains sensitive information such as the API key
import secret

# Importing everything in the colors 3rd party module, which is used for changing the color of the CLI text.
from colors import *

def get_btc_price():
    """
    Fetches the current Bitcoin (BTC) price in AUD using the CoinMarketCap API.

    Returns:
        float: The current price of 1 BTC in AUD.
    """

    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": "BTC",    # Specifies the cryptocurrency to retrieve data for (Bitcoin in this case)
        "convert": "AUD"    # Specifies the currency to convert the price into (Australian Dollars)
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
    
    """
    Reads the CSV file and calculates the total BTC holdings from the data.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        float: The total BTC holdings from the CSV file.
    """

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
    
    """
    Calculates the total AUD value of the user's BTC holdings.

    Args:
        btc_price (float): The current price of 1 BTC in AUD.
        btc_holdings (float): The total BTC holdings.

    Returns:
        float: The AUD value of the BTC holdings.
    """
    
    aud_value = btc_price * btc_holdings
    return aud_value