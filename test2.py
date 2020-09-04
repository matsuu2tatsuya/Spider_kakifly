import requests
import pandas as pd
import re

base_url = 'https://tokentrove.com/GodsUnchainedCards/'
request_url = 'https://api.tokentrove.com/cached/all-orders'
payload = {'tokenAddress': '0x0e3a2a1f2146d86a604adc220b4967a898d7fe07'}
x_api_key = 'Np8BV2d5QR9TSFEr9EvF66FWcJf0wIxy2qBpOH6s'
headers = {'x-api-key': x_api_key,
           'User-Agent': 'PostmanRuntime/7.25.0'}

response = requests.request("GET", request_url, params=payload, headers=headers).json()

name = []
price = []
currency = []
quality = []
purchase_URL = []
image_URL = []

for res in response:
    id = re.sub(r'-.', '', res['token_proto'])

    name.append(id)
    price.append(str(round((res['takerAssetAmount'] / 10**18) * 102.5, 4)))
    currency.append('ETH')
    quality.append(res['token_proto'][-1])
    purchase_URL.append(base_url + res['token_proto'])
    image_URL.append(f'https://card.godsunchained.com/?id={id}&q={res["token_proto"][-1]}&w=512&png=true')


df = pd.DataFrame(
    data={'name': name, 'price': price, 'currency': currency,
          'quality': quality, 'purchase_URL': purchase_URL, 'image_URL': image_URL},
    columns=['name', 'price', 'currency', 'quality', 'purchase_URL', 'image_URL']
)

df.to_csv('example.csv', index=False)


