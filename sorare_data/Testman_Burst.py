import re
import requests
import csv
import pandas as pd
from enum import IntEnum, auto
import json


text = """
| https://sorare.com/cards/kevin-paredes-2020-rare-7                    |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-49            |
| https://sorare.com/cards/odisseas-vlachodimos-2019-super_rare-7       |
| https://sorare.com/cards/odisseas-vlachodimos-2019-super_rare-4       |
| https://sorare.com/cards/fyodor-smolov-2020-super_rare-4              |
| https://sorare.com/cards/francisco-reis-ferreira-2019-super_rare-7    |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-super_rare-5 |
| https://sorare.com/cards/jong-jin-kim-1996-03-05-2020-rare-1          |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-7       |
| https://sorare.com/cards/kang-in-lee-2019-rare-26                     |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-70      |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-45               |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-72            |
| https://sorare.com/cards/fyodor-smolov-2020-super_rare-3              |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-49             |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-68      |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-17             |
| https://sorare.com/cards/francisco-reis-ferreira-2019-rare-11         |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-14      |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-45             |
| https://sorare.com/cards/joao-pedro-neves-filipe-2019-rare-31         |
| https://sorare.com/cards/kang-in-lee-2019-rare-29                     |
| https://sorare.com/cards/francisco-reis-ferreira-2019-rare-74         |
| https://sorare.com/cards/marvelous-nakamba-2018-rare-8                |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-3       |
| https://sorare.com/cards/marcus-schubert-2019-rare-38                 |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-29             |
| https://sorare.com/cards/gordan-bunoza-2020-rare-5                    |
| https://sorare.com/cards/virgiliu-postolachi-2020-rare-2              |
| https://sorare.com/cards/yvan-neyou-noupa-2020-rare-1                 |
| https://sorare.com/cards/munir-mercan-2019-rare-15                    |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-42               |
| https://sorare.com/cards/kekuta-manneh-2020-rare-7                    |
| https://sorare.com/cards/wilfried-aimeric-zahibo-2020-rare-7          |
| https://sorare.com/cards/antonio-barragan-fernandez-2019-super_rare-2 |
| https://sorare.com/cards/marcus-schubert-2019-super_rare-7            |
| https://sorare.com/cards/edgar-gonzalez-estrada-2019-super_rare-1     |
| https://sorare.com/cards/isaac-kiese-thelin-2019-rare-2               |
| https://sorare.com/cards/byung-chan-choi-2020-rare-2                  |
| https://sorare.com/cards/byung-chan-choi-2020-rare-4                  |
| https://sorare.com/cards/kang-in-lee-2019-rare-33                     |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-24             |
| https://sorare.com/cards/gordan-bunoza-2020-rare-4                    |
| https://sorare.com/cards/kekuta-manneh-2020-rare-2                    |
| https://sorare.com/cards/cedric-gogoua-kouame-2019-rare-8             |
| https://sorare.com/cards/nill-de-pauw-2018-rare-3                     |
| https://sorare.com/cards/jin-kyu-song-1997-07-12-2020-rare-1          |
| https://sorare.com/cards/kevin-paredes-2020-rare-6                    |
| https://sorare.com/cards/kang-in-lee-2019-rare-8                      |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-38            |
| https://sorare.com/cards/munir-mercan-2019-rare-7                     |
| https://sorare.com/cards/wilfried-aimeric-zahibo-2020-rare-5          |
| https://sorare.com/cards/kang-in-lee-2019-super_rare-9                |
| https://sorare.com/cards/munir-mercan-2019-rare-24                    |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-46               |
| https://sorare.com/cards/kang-in-lee-2020-rare-1                      |
"""

price1 = re.sub(r'\|', '', text)
price2 = re.sub(r' ', '', price1)
price4 = re.sub(r'https://sorare.com/cards/', '', price2)
price5 = re.sub(r'-20.*', '', price4)
price3 = price5.split('\n')
price3.pop(0)
price3.pop(-1)

list = list(set(price3))
print(len(list))

class Position(IntEnum):
    Defender = auto()
    Midfielder = auto()
    Forward = auto()
    Goalkeeper = auto()
    Coach = auto()


for i in list:
    sub_query = """
    query
    {player(slug:"OreNoCursor"),{displayName,position,activeClub{name}}}
    """
    sub_query = re.sub(r'OreNoCursor', f'{i}', sub_query)
    url = 'https://api.sorare.com/graphql'
    r = requests.post(url, json={'query': sub_query})
    json_data = json.loads(r.text)
    data = json_data['data']
    print(data)
    position = data['player']['position']

    with open('newCardData', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(
            [f"{data['player']['displayName']}", f"{Position[position].value}",
             f"{data['player']['activeClub']['name']}"])
