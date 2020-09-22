import requests
import json
import re

def get_cursor(point):
    query = f""" 
    query 
    {{auctions(after:"{point}"){{edges{{cursor}}}}}}
    """
    url = 'https://api.sorare.com/graphql'
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    for i in json_data['data']['auctions']['edges']:
        cursor_list.append(i['cursor'])
    return cursor_list

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

cursor_list = []
get_cursor('')

while cursor_list[-1]:
    # 重複するかどうかを確認
    CheckOne = len(cursor_list)
    CheckTwo = len(get_cursor(cursor_list[-1]))
    if CheckOne == CheckTwo:
        break

sorare_list = []
for i in cursor_list:
    get_Sorare_data(i)
    print(i)
    print(len(get_Sorare_data(i)))

with open('./sorare.json', 'w') as f:
    json.dump(sorare_list, f, indent=2)
