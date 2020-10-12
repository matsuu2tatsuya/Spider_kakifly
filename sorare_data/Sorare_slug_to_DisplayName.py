import csv
import json
import re
import requests

with open('Card_Name.csv') as f:
    writer = csv.reader(f)
    for i in writer:
        sub_query = """
        query
        {player(slug:"OreNoCursor"),{birthDate,displayName}}
        """
        sub_query = re.sub(r'OreNoCursor', f'{i[0]}', sub_query)
        url = 'https://api.sorare.com/graphql'
        r = requests.post(url, json={'query': sub_query})
        json_data = json.loads(r.text)
        with open('Card_Name2.csv', 'a') as k:
            writ = csv.writer(k)
            writ.writerow([f'{i[0]}', f'{json_data["data"]["player"]["displayName"]}'])
        print(json_data)
