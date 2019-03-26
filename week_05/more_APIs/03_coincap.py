'''
Sign up for an API key with the new coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.

'''

from bl import coin_key
from pprint import pprint
# This example uses Python 2.7+ and the python-request library
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'convert': 'USD',
    'sort': 'price',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coin_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = (response.json())
    # pprint(data)
    with open('coincap.json', 'a') as file_object:
        for coin in data['data']:
            file_object.write(f"{coin['cmc_rank']}\n")
            file_object.write(f"{coin['name']}\n")
            file_object.write(f"{coin['symbol']}\n")
            file_object.write(f"{coin['platform']}\n")
            file_object.write(f"{coin['quote']}\n")
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)







