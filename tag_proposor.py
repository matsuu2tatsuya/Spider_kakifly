import requests
import json
import re


sub_query = """
query
{auctions(after:"OreNoCursor"){pageInfo{hasNextPage,startCursor},nodes{bidsCount,card{club{name,pictureUrl},
createdAt,edition,grade,name,onSale,pictureUrl,position,power,price,rarity}
,currentPrice,endDate,id,minNextBid,name,number,open}}}
"""
sub_query = re.sub(r'OreNoCursor', 'Mg', sub_query)
print(sub_query)
# url = 'https://api.sorare.com/graphql'
# r = requests.post(url, json={'query': sub_query})
# json_data = json.loads(r.text)
# print(json_data)
