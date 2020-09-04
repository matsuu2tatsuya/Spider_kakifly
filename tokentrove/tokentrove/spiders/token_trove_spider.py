# -*- coding: utf-8 -*-
from ..items import TokentroveItem
import re
from selenium.webdriver import Chrome, ChromeOptions
import scrapy
from scrapy.crawler import CrawlerProcess
import requests

# 下記の変数は保守性を考えた上です。

def custom_settings(pages):
    return {
        'BOT_NAME': 'tokentrove',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'tokentrove.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['tokentrove.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'tokenTrove.json',
        'USER_AGENT': 'Mozilla/5.0'

    }

class TokenTrove_1_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    custom_settings = custom_settings(1)
    start_urls = ['https://tokentrove.com/']

    def parse(self, response):
        item = TokentroveItem()
        base_url = 'https://tokentrove.com/GodsUnchainedCards/'
        request_url = 'https://api.tokentrove.com/cached/all-orders'
        payload = {'tokenAddress': '0x0e3a2a1f2146d86a604adc220b4967a898d7fe07'}
        x_api_key = 'Np8BV2d5QR9TSFEr9EvF66FWcJf0wIxy2qBpOH6s'
        headers = {'x-api-key': x_api_key,
                   'User-Agent': 'Mozilla/5.0'}

        for res in requests.request("GET", request_url, params=payload, headers=headers).json()[0]:
            print(res)
            id = re.sub(r'-.', '', res['token_proto'])
            quality = re.sub(r'.*-', '', res['token_proto'])
            item['name'] = id
            item['price'] = (res['takerAssetAmount'] / 10*18) * 102.5
            item['currency'] = 'ETH'
            item['quality'] = quality
            item['purchase_URL'] = base_url + res['token_proto']
            item['image_URL'] = f'https://card.godsunchained.com/?id={id}&q={quality}&w=512&png=true'

            yield item

def handler():
    process = CrawlerProcess()
    process.crawl(TokenTrove_1_Spider)
    process.start()

