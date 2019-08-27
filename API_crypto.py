# Import relevant python modules

import requests
import pandas as pd
url = 'https://rest.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key' : 'E22EE934-CF7C-45B7-AB10-CBAF5E04C98D'}
response = requests.get(url, headers=headers)

# Convert Json response to a dictionary
crypto_exchange_values = response.json()

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


df_crypto_exchange_values = pd.DataFrame.from_dict(crypto_exchange_values)

print(df_crypto_exchange_values.head())
print(df_crypto_exchange_values.count())
