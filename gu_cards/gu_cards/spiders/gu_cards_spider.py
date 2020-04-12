from ..items import GuCardsItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess

"""
gu_cardsのみでspiderを作る。
selenium以外で(200)レスポンスを受け取る方法がわからない、他だと403エラーが帰ってくる。
かつページがNextボタンで次のページに行く仕様のため、selenium_middlewareを大量に用意して、scrapyを走らせることにする。
//WARN::(別の方法を考えた方が全てにおいていいが、現状解決策がないため、質問できる人に聞くべき。)
"""

# 下記の変数は保守性を考えた上です。
all_cards = 'div.js-card-with-trading-buttons'
name_base = 'div.card-name-cell > span'
price_base = 'button.js-buy-button > span'
ETH = 'ETH'
Shadow = 'Shadow'        # quality_id = 3
Gold = 'Gold'            # quality_id = 2
Diamond = 'Diamond'      # quality_id = 1
base_url = 'https://gu.cards/'
purchase_URL_base = 'a.js-card-link::attr("href")'

def image_URL_base(card_id, quality_id):
    return f'https://card.godsunchained.com/?id={card_id}&q={quality_id}&w=256&png=true'

# ここまでが変数ゾーンです。 ここから下は大量のspider作っていきます。

# Shadow
class guCardsShadow_1_Spider(scrapy.Spider):
    name = 'guCardsShadow_1_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_1_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

class guCardsShadow_2_Spider(scrapy.Spider):
    name = 'guCardsShadow_2_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_2_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

class guCardsShadow_3_Spider(scrapy.Spider):
    name = 'guCardsShadow_3_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_3_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

class guCardsShadow_4_Spider(scrapy.Spider):
    name = 'guCardsShadow_4_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_4_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

class guCardsShadow_5_Spider(scrapy.Spider):
    name = 'guCardsShadow_5_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_5_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

class guCardsShadow_6_Spider(scrapy.Spider):
    name = 'guCardsShadow_6_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_6_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

class guCardsShadow_7_Spider(scrapy.Spider):
    name = 'guCardsShadow_7_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {'gu_cards.middlewares.guCardsShadow_7_Middleware': 520},
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsShadow.json',
    }

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Shadow
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 3)

            yield item

def handler():
    process = CrawlerProcess()

    process.crawl(guCardsShadow_1_Spider)
    process.crawl(guCardsShadow_2_Spider)
    process.crawl(guCardsShadow_3_Spider)
    process.crawl(guCardsShadow_4_Spider)
    process.crawl(guCardsShadow_5_Spider)
    process.crawl(guCardsShadow_6_Spider)
    process.crawl(guCardsShadow_7_Spider)

    process.start()

