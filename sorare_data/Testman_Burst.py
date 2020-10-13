import re
import requests
import csv
import pandas as pd
from enum import IntEnum, auto
import json


text = """
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-19      |
| https://sorare.com/cards/marcus-schubert-2019-super_rare-7            |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-24             |
| https://sorare.com/cards/gian-luca-waldschmidt-2020-rare-3            |
| https://sorare.com/cards/marcus-schubert-2019-rare-44                 |
| https://sorare.com/cards/munir-mercan-2019-rare-7                     |
| https://sorare.com/cards/francisco-reis-ferreira-2019-super_rare-6    |
| https://sorare.com/cards/jose-luis-gaya-pena-2020-super_rare-1        |
| https://sorare.com/cards/jan-vertonghen-2020-rare-2                   |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-38            |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2020-rare-2       |
| https://sorare.com/cards/kang-in-lee-2020-rare-1                      |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-56               |
| https://sorare.com/cards/munir-mercan-2019-rare-14                    |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-37      |
| https://sorare.com/cards/munir-mercan-2019-rare-24                    |
| https://sorare.com/cards/kevin-paredes-2020-rare-7                    |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-49            |
| https://sorare.com/cards/odisseas-vlachodimos-2019-super_rare-7       |
| https://sorare.com/cards/odisseas-vlachodimos-2019-super_rare-4       |
| https://sorare.com/cards/diogo-antonio-cupido-goncalves-2020-rare-5   |
| https://sorare.com/cards/fyodor-smolov-2020-super_rare-4              |
| https://sorare.com/cards/francisco-reis-ferreira-2019-super_rare-7    |
| https://sorare.com/cards/maksym-malyshev-2020-rare-1                  |
| https://sorare.com/cards/hiroyuki-abe-2020-rare-7                     |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-super_rare-5 |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-7       |
| https://sorare.com/cards/kang-in-lee-2019-rare-26                     |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-70      |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-45               |
| https://sorare.com/cards/chang-yong-lee-2020-rare-6                   |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-72            |
| https://sorare.com/cards/fyodor-smolov-2020-super_rare-3              |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-49             |
| https://sorare.com/cards/helton-brant-aleixo-leite-2020-rare-2        |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-68      |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-17             |
| https://sorare.com/cards/diogo-antonio-cupido-goncalves-2020-rare-4   |
| https://sorare.com/cards/francisco-reis-ferreira-2019-rare-11         |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-14      |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-45             |
| https://sorare.com/cards/joao-pedro-neves-filipe-2019-rare-31         |
| https://sorare.com/cards/maksym-malyshev-2020-rare-3                  |
| https://sorare.com/cards/kang-in-lee-2019-rare-29                     |
| https://sorare.com/cards/pedro-victor-delmino-da-silva-2020-rare-3    |
| https://sorare.com/cards/francisco-reis-ferreira-2019-rare-74         |
| https://sorare.com/cards/chang-yong-lee-2020-rare-10                  |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-3       |
| https://sorare.com/cards/marcus-schubert-2019-rare-38                 |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-29             |
| https://sorare.com/cards/hiroyuki-abe-2020-rare-8                     |
| https://sorare.com/cards/gilberto-moraes-junior-2020-rare-6           |
| https://sorare.com/cards/virgiliu-postolachi-2020-rare-2              |
| https://sorare.com/cards/yvan-neyou-noupa-2020-rare-1                 |
| https://sorare.com/cards/munir-mercan-2019-rare-15                    |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-42               |
| https://sorare.com/cards/kevin-paredes-2020-rare-6                    |
| https://sorare.com/cards/michael-heylen-2019-super_rare-1             |
| https://sorare.com/cards/gilberto-moraes-junior-2020-rare-1           |
| https://sorare.com/cards/munir-mercan-2019-rare-14                    |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-37      |
| https://sorare.com/cards/kevin-paredes-2020-rare-7                    |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-49            |
| https://sorare.com/cards/odisseas-vlachodimos-2019-super_rare-7       |
| https://sorare.com/cards/odisseas-vlachodimos-2019-super_rare-4       |
| https://sorare.com/cards/diogo-antonio-cupido-goncalves-2020-rare-5   |
| https://sorare.com/cards/fyodor-smolov-2020-super_rare-4              |
| https://sorare.com/cards/francisco-reis-ferreira-2019-super_rare-7    |
| https://sorare.com/cards/hiroyuki-abe-2020-rare-7                     |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-super_rare-5 |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-7       |
| https://sorare.com/cards/kang-in-lee-2019-rare-26                     |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-70      |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-45               |
| https://sorare.com/cards/chang-yong-lee-2020-rare-6                   |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-72            |
| https://sorare.com/cards/fyodor-smolov-2020-super_rare-3              |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-49             |
| https://sorare.com/cards/helton-brant-aleixo-leite-2020-rare-2        |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-68      |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-17             |
| https://sorare.com/cards/diogo-antonio-cupido-goncalves-2020-rare-4   |
| https://sorare.com/cards/francisco-reis-ferreira-2019-rare-11         |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-14      |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-45             |
| https://sorare.com/cards/joao-pedro-neves-filipe-2019-rare-31         |
| https://sorare.com/cards/maksym-malyshev-2020-rare-3                  |
| https://sorare.com/cards/kang-in-lee-2019-rare-29                     |
| https://sorare.com/cards/pedro-victor-delmino-da-silva-2020-rare-3    |
| https://sorare.com/cards/francisco-reis-ferreira-2019-rare-74         |
| https://sorare.com/cards/chang-yong-lee-2020-rare-10                  |
| https://sorare.com/cards/maximiliano-gomez-gonzalez-2019-rare-3       |
| https://sorare.com/cards/marcus-schubert-2019-rare-38                 |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-29             |
| https://sorare.com/cards/hiroyuki-abe-2020-rare-8                     |
| https://sorare.com/cards/gilberto-moraes-junior-2020-rare-6           |
| https://sorare.com/cards/virgiliu-postolachi-2020-rare-2              |
| https://sorare.com/cards/yvan-neyou-noupa-2020-rare-1                 |
| https://sorare.com/cards/munir-mercan-2019-rare-15                    |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-42               |
| https://sorare.com/cards/michael-heylen-2019-super_rare-1             |
| https://sorare.com/cards/marcus-schubert-2019-super_rare-7            |
| https://sorare.com/cards/helton-brant-aleixo-leite-2020-rare-4        |
| https://sorare.com/cards/kang-in-lee-2019-rare-33                     |
| https://sorare.com/cards/grant-lillard-2020-rare-3                    |
| https://sorare.com/cards/jose-luis-gaya-pena-2019-rare-24             |
| https://sorare.com/cards/gian-luca-waldschmidt-2020-rare-3            |
| https://sorare.com/cards/kevin-paredes-2020-rare-6                    |
| https://sorare.com/cards/kang-in-lee-2019-rare-8                      |
| https://sorare.com/cards/odisseas-vlachodimos-2019-rare-38            |
| https://sorare.com/cards/maksym-malyshev-2020-rare-5                  |
| https://sorare.com/cards/munir-mercan-2019-rare-7                     |
| https://sorare.com/cards/jan-vertonghen-2020-rare-2                   |
| https://sorare.com/cards/kang-in-lee-2019-super_rare-9                |
| https://sorare.com/cards/maksym-malyshev-2020-rare-1                  |
| https://sorare.com/cards/munir-mercan-2019-rare-24                    |
| https://sorare.com/cards/mehmet-zeki-celik-2019-rare-46               |
"""

price1 = re.sub(r'\|', '', text)
price2 = re.sub(r' ', '', price1)
price4 = re.sub(r'https://sorare.com/cards/', '', price2)
price5 = re.sub(r'-20.*', '', price4)
price3 = price5.split('\n')
price3.pop(0)
price3.pop(-1)

list = list(set(price3))

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
