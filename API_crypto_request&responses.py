# Import relevant python modules

import requests
import pandas as pd

# Connecting with CoinAPI.io
""" find documentation at https://docs.coinapi.io/?python#introduction """
url = 'https://rest.coinapi.io/v1/<DEPENDING ON WHICH DATA TO BE RETRIEVED>'
headers = {'X-CoinAPI-Key' : '<API-KEY>'}
response = requests.get(url, headers=headers)
# Convert Json response to a dictionary
crypto_exchange_values = response.json()

# Request 1 - Get a detailed list of exchanges provided by the system
url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key' : 'E22EE934-CF7C-45B7-AB10-CBAF5E04C98D'}
response_1 = requests.get(url, headers=headers)

# Convert Json response to a dictionary
crypto_exchange_info = response_1.json()

# The following line is a web preview of our Json request
# https://rest.coinapi.io/v1/exchanges?apikey=E22EE934-CF7C-45B7-AB10-CBAF5E04C98D

# Request 2 - Get exchange rate between pair of requested assets at specific or current time.
""" GET /v1/exchangerate/<asset_id_base>/<asset_id_quote>?time=<time> (time is optional, current by default)"""

url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key' : 'E22EE934-CF7C-45B7-AB10-CBAF5E04C98D'}
response_2 = requests.get(url, headers=headers)

# Convert Json response to a dictionary
crypto_exchangerate_BTC_USD = response_2.json()

# The following line is a web preview of our Json request
# https://rest.coinapi.io/v1/exchangerate/BTC?apikey=E22EE934-CF7C-45B7-AB10-CBAF5E04C98D

# Preview the first key-value pair
#i = 0
#for key, value in crypto_exchange_values :
#    print(key + ' : ' + value)

#    if i == 5 :
#        break
#    else :
#        i += 1


df_crypto_exchange_info = pd.DataFrame.from_dict(crypto_exchange_info)

df_crypto_exchangerate_BTC_USD = pd.DataFrame.from_dict(crypto_exchangerate_BTC_USD)

print(df_crypto_exchange_values.head())
print(df_crypto_exchange_values.count())

print(df_crypto_exchangerate_BTC_USD.head())
print(df_crypto_exchangerate_BTC_USD.count())
