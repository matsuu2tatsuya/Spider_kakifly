import requests
import json
import re

def get_Sorare_data(cursor):
    sub_query = """
    query
    {auctions(after:"OreNoCursor"){pageInfo{hasNextPage,startCursor},nodes{bidsCount,card{club{name,pictureUrl},
    createdAt,edition,grade,name,onSale,pictureUrl,position,power,price,rarity}
    ,currentPrice,endDate,id,minNextBid,name,number,open}}}
    """
    sub_query = re.sub(r'OreNoCursor', cursor, sub_query)
    url = 'https://api.sorare.com/graphql'
    r = requests.post(url, json={'query': sub_query})
    json_data = json.loads(r.text)
    for i in json_data['data']['auctions']['nodes']:
        sorare_list.append(i)
    return sorare_list

for i in ['Mg', 'NTA']:
    get_Sorare_data(i)
