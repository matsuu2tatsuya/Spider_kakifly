import requests
import json
import re

# def get_cursor(point):
#     query = f"""
#     query
#     {{singleSaleOffers(after:"{point}"){{pageInfo{{endCursor}}}}}}
#     """
#     url = 'https://api.sorare.com/graphql'
#     r = requests.post(url, json={'query': query})
#     json_data = json.loads(r.text)
#     i = json_data['data']['singleSaleOffers']['pageInfo']
#     if i['endCursor']:
#         cursor_list.append(i['endCursor'])
#     return cursor_list

# cursor_list = []
# get_cursor('')

# while cursor_list[-1]:
#     # 重複するかどうかを確認
#     CheckOne = len(cursor_list)
#     CheckTwo = len(get_cursor(cursor_list[-1]))
#     if CheckOne == CheckTwo:
#         break
# print(cursor_list)
# print(len(cursor_list))


def get_Sorare_data(cursor):
    sub_query = """
    query
    {singleSaleOffers(after:"OreNoCursor")
    {pageInfo{hasNextPage,endCursor},
    nodes{endDate,card{club{domesticLeague{name},name,pictureUrl},
    edition,name,pictureUrl,position,power,price,rarity,season{name},serialNumber,slug}}}}
    """
    sub_query = re.sub(r'OreNoCursor', cursor, sub_query)
    url = 'https://api.sorare.com/graphql'
    r = requests.post(url, json={'query': sub_query})
    json_data = json.loads(r.text)
    curs = json_data['data']['singleSaleOffers']['pageInfo']
    for i in json_data['data']['singleSaleOffers']['nodes']:
        sorare_list.append(i)
    return curs['hasNextPage'], curs['endCursor']

sorare_list = []
i, k = get_Sorare_data("")
while i:
    i, k = get_Sorare_data(k)
    print(i)
    print(k)
if not i:
    i, k = get_Sorare_data(k)


with open('./sorare.json', 'w') as f:
    json.dump(sorare_list, f, indent=2)
