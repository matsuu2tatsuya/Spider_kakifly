# -*- coding: utf-8 -*-
from ..items import TokentroveItem
import scrapy
import re
import scrapy
from scrapy.crawler import CrawlerProcess

# 下記の変数は保守性を考えた上です。
all_cards = 'div.js-card-with-trading-buttons'
name_base = 'div.card-name-cell > span'
price_base = 'button.js-buy-button > span'
ETH = 'ETH'
Meteorite = 'Meteorite'  # quality_id = 4

def custom_settings(quality, pages):
    return {
        "DOWNLOADER_MIDDLEWARES": {
            'tokentrove.middlewares.tokentrove_Selenium_Middleware': 540,
        },
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
        # 'FEED_FORMAT': 'json',
        # 'FEED_URI': 'tokentrove.json',
    }

def quality_id(id):
    if id == '1':
        return 'Diamond'
    elif id == '2':
        return 'Gold'
    elif id == '3':
        return 'Shadow'
    elif id == '4':
        return 'Meteorite'
    else:
        return 'Plain'

def purchase_URL_base(card_id, quality_id):
    return f'https://tokentrove.com/GodsUnchainedCards/{card_id}-{quality_id}'

def image_URL_base(card_id, quality_id):
    return f'https://card.godsunchained.com/?id={card_id}&q={quality_id}&w=256&png=true'

# ここまでが変数ゾーンです。 ここから下は大量のspider作っていきます。



class TokenTrove_1_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings()

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string').get()

            # item['price'] = res.css('gu-heading-text.cardItemFooter__price').xpath('string()').get()
            #
            # item['currency'] = 'ETH'
            # item['quality'] = 'Plain'
            #
            # item['purchase_URL'] = base_purchase_url(name_id, quality_id, 'your_contract_number')
            # item['image_URL'] = base_url

            yield item


def handler():
    process = CrawlerProcess()
    process.crawl(TokenTrove_1_Spider)
    process.start()

