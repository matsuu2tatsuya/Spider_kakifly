import requests

url = "https://api.opensea.io/api/v1/assets"

querystring = {
    "asset_contract_address": "0x0e3a2a1f2146d86a604adc220b4967a898d7fe07",
    "asset_contract_addresses": "[]",
    "order_direction": "desc",
    "on_sale": "true",
    "offset": "0",
    "limit": "20"}

response = requests.request("GET", url, params=querystring)

print(response.text)
