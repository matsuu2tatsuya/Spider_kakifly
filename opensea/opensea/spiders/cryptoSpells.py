# -*- coding: utf-8 -*-
import scrapy
import re
import requests
import json
from ..items import OpenseaItem

class CryptospellsSpider(scrapy.Spider):
    name = 'cryptoSpells'
    allowed_domains = ['api.opensea.io']
    start_urls = ['https://api.opensea.io/api/v1/assets/']

    custom_settings = {
        'BOT_NAME': 'opensea',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'opensea.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['opensea.spiders'],
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'CryptoSpells_OpenSea.csv',
    }

    def parse(self, response):
        item = OpenseaItem()
        contract = 'asset_contract_address=0x67cbbb366a51fff9ad869d027e496ba49f5f6d55'
        asset_ID = 0

        for set in range(0, 1000, 50):
            response = requests.get(f'https://api.opensea.io/api/v1/assets?{contract}&on_sale=true&limit=1000&offset={set}').json()
            if not response['assets']:
                break
            else:
                for res in response['assets']:
                    item['name'] = res['name']
                    item['currency'] = 'ETH'
                    price = float(res['sell_orders'][0]['current_price']) / 10 ** 18
                    item['price'] = round(price, 4)
                    item['image_URL'] = res['image_url']
                    item['purchase_URL'] = res['permalink']
                    item['asset_ID'] = asset_ID
                    asset_ID += 1

                    yield item

