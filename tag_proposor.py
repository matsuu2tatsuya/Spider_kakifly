import requests
import json
import re


def fetch_Sorare_API():
    sub_query = """
    query
    {allCards(after:"OreNoCursor"){pageInfo{hasNextPage,endCursor},nodes{club{name,pictureUrl,
    domesticLeague{name,pictureUrl}},edition,name,pictureUrl,position,power,rarity,slug,season{name}}}}
    """
    return re.sub(r'OreNoCursor', 'Mg', sub_query)


url = 'https://api.sorare.com/graphql'
r = requests.post(url, json={'query': sub_query})
json_data = json.loads(r.text)
print(json_data)
