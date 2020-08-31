#最近の投稿10件のうち最も使われた上位n件のタグを出力します

import json
import re
import itertools
import collections

import urllib.parse as urlparse
from urllib.parse import urlencode

import requests
import pprint

url = "https://graph.facebook.com/v6.0/17841438910663891"
params = {
    'fields': 'name,media{caption,media_url,permalink,timestamp,username,like_count}',
    'access_token': 'EAAKiVaUhBhEBAEqisclBrCy19m3oe4kdDBhcmqn0ca9UIbDZB1HwfZBqc0E5fneQH0ZByPfOkLunMaren2dDZAUbZAF5BTUepYZBnlmEbo3KPgvZCNs5ufXH2EfqIfoggtZB3Sa3DGRcIZCWEZAJrGAl3MwpasPrN8cFaNIvqY0RdFzL45bwZAtFNJZC6OQy75xlTZCehKylrpZBQ5JbqFuLdKWyZCfeLI8YLKkykRsMCyAyNMd5wZDZD',
    }

url_parts = list(urlparse.urlparse(url))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)

url_parts[4] = urlencode(query)
url=urlparse.urlunparse(url_parts)

response = requests.get(url)
data = response.json()

tag_list = []
for post in data["media"]["data"][:10]:
    try:
        str = post["caption"]
        start = str.find("#")
        str = str[start:].replace("\n", "").replace(" ", "")
        tag_list.append(str.split("#")[1:])
    except KeyError:
        print("***")

tag_list_flatten = list(itertools.chain.from_iterable(tag_list))
c = collections.Counter(tag_list_flatten)

try:
    num = int(input('使われたタグのうち、上位n件出力します \n input n \n'))
except ValueError:
    print("整数を入れてください")
    num = 3
proposing_tags, cnt = zip(*c.most_common())

print(proposing_tags[:num])
