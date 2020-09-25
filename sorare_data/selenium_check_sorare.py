import requests
import json
import re
import pandas as pd


asset_ID = 301000000
asset = []
endDate = []
club_League = []
club_name = []
club_image = []
edition = []
name = []
pictureUrl = []
position = []
power = []
price = []
rarity = []
season = []
serialNumber = []
purchaese_url = []

base_url = 'https://sorare.com/cards/'
request_url = 'https://api.sorare.com/graphql'
query = """query
{singleSaleOffers(after:"OreNoCursor")
{pageInfo{hasNextPage,endCursor},
nodes{endDate,card{club{domesticLeague{name},name,pictureUrl},
edition,name,pictureUrl,position,power,price,rarity,season{name},serialNumber,slug}}}}
"""
cursor = ''
while cursor != False:
    try:
        real_query = re.sub(r'OreNoCursor', cursor, query)
    except Exception as e:
        br
    response = requests.post(request_url, json={'query': real_query})
    json_data = json.loads(response.text)
    curs = json_data['data']['singleSaleOffers']['pageInfo']
    for i in json_data['data']['singleSaleOffers']['nodes']:
        asset.append(str(asset_ID))
        asset_ID += 1
        endDate.append(i['endDate'])
        club_League.append(i['card']['club']['domesticLeague']['name'])
        club_name.append(i['card']['club']['name'])
        club_image.append(i['card']['club']['pictureUrl'])
        edition.append(i['card']['edition'])
        name.append(i['card']['name'])
        pictureUrl.append(i['card']['pictureUrl'])
        position.append(i['card']['position'])
        power.append(i['card']['power'])
        price.append(i['card']['price'])
        rarity.append(i['card']['rarity'])
        season.append(i['card']['season']['name'])
        serialNumber.append(i['card']['serialNumber'])
        purchaese_url.append(base_url + i['card']['slug'])
    cursor = curs['endCursor']
    print(cursor)

df = pd.DataFrame(
    data={'asset_ID': asset, 'endDate': endDate, 'club_League': club_League, 'club_name': club_name,
          'club_image': club_image, 'edition': edition, 'name': name, 'pictureUrl': pictureUrl,
          'position': position,
          'power': power, 'price': price, 'rarity': rarity, 'season': season, 'serialNumber': serialNumber,
          'purchaese_url': purchaese_url
          },
    columns=['asset_ID', 'endDate', 'club_League', 'club_name', 'club_image', 'edition', 'name', 'pictureUrl',
             'position', 'power', 'price', 'rarity', 'season', 'serialNumber', 'purchaese_url']
)

print(df)

