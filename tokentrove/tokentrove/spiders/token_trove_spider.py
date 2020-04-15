# -*- coding: utf-8 -*-
from ..items import TokentroveItem
import scrapy
import re
import scrapy
from scrapy.crawler import CrawlerProcess

# 下記の変数は保守性を考えた上です。

def custom_settings(pages):
    return {
        "DOWNLOADER_MIDDLEWARES": {
            f'tokentrove.middlewares.tokentrove_{pages}_Selenium_Middleware': 540,
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
        # 'FEED_URI': 'tokenTrove.json',
    }

def quality_id(q_id):
    if q_id == '1':
        return 'Diamond'
    elif q_id == '2':
        return 'Gold'
    elif q_id == '3':
        return 'Shadow'
    elif q_id == '4':
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
    custom_settings = custom_settings(1)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_2_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(2)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_3_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(3)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_4_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(4)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_5_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(5)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_6_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(6)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_7_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(7)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_8_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(8)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_9_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(9)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_10_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(10)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_11_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(11)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_12_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(12)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_13_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(13)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_14_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(14)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item

class TokenTrove_15_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(15)

    def parse(self, response):
        item = TokentroveItem()
        for res in response.css('div.listing-wrapper'):
            item['name'] = res.css('div.listing-name').xpath('string()').get()
            base_price = res.css('div.listing-price').xpath('string()').get()
            item['price'] = re.sub(r'\D*', '', base_price)
            item['currency'] = 'ETH'
            q_id = res.css('composited-card::attr("quality")').get()
            item['quality'] = quality_id(q_id)
            c_id = res.css('composited-card::attr("protoid")').get()
            item['purchase_URL'] = purchase_URL_base(c_id, q_id)
            item['image_URL'] = image_URL_base(c_id, q_id)

            yield item


def handler():
    process = CrawlerProcess()
    process.crawl(TokenTrove_1_Spider)
    process.crawl(TokenTrove_2_Spider)
    process.crawl(TokenTrove_3_Spider)
    process.crawl(TokenTrove_4_Spider)
    process.crawl(TokenTrove_5_Spider)
    process.crawl(TokenTrove_6_Spider)
    process.crawl(TokenTrove_7_Spider)
    process.crawl(TokenTrove_8_Spider)
    process.crawl(TokenTrove_9_Spider)
    process.crawl(TokenTrove_10_Spider)
    process.crawl(TokenTrove_11_Spider)
    process.crawl(TokenTrove_12_Spider)
    process.crawl(TokenTrove_13_Spider)
    process.crawl(TokenTrove_14_Spider)
    process.crawl(TokenTrove_15_Spider)
    process.start()

