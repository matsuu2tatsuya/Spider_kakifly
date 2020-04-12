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
Meteorite = 'Meteorite'  # quality_id = 4
base_url = 'https://gu.cards/'
purchase_URL_base = 'a.js-card-link::attr("href")'

def custom_settings(quality, pages):
    return {
        "DOWNLOADER_MIDDLEWARES": {f'gu_cards_meteorite.middlewares.guCards{quality}_{pages}_Middleware': 520},
        'BOT_NAME': 'gu_cards_meteorite',
        'NEWSPIDER_MODULE': 'gu_cards_meteorite.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gu_cards_meteorite.spiders'],
        'USER_AGENT': 'gu_cards_meteorite (+http://www.yourdomain.com)',
        'CONCURRENT_REQUESTS': 16,
        'DOWNLOAD_DELAY': 1,
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": 'guCardsMeteorite.json',
    }

def image_URL_base(card_id, quality_id):
    return f'https://card.godsunchained.com/?id={card_id}&q={quality_id}&w=256&png=true'

# ここまでが変数ゾーンです。 ここから下は大量のspider作っていきます。

# Meteorite
class guCardsMeteorite_1_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_1_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 1)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_2_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_2_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 2)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_3_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_3_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 3)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_4_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_4_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 4)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_5_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_5_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 5)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_6_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_6_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 6)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_7_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_7_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 7)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_8_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_8_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 8)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_9_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_9_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 9)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_10_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_10_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 10)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_11_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_11_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 11)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_12_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_12_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 12)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_13_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_13_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 13)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 5)

            yield item

class guCardsMeteorite_14_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_14_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 14)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_15_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_15_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 15)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_16_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_16_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 16)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item

class guCardsMeteorite_17_Spider(scrapy.Spider):
    name = 'guCardsMeteorite_17_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']
    custom_settings = custom_settings(Meteorite, 17)

    def parse(self, response):
        for res in response.css(all_cards):
            item = GuCardsItem()
            item['name'] = res.css(name_base).xpath('string()').get()
            item['price'] = res.css(price_base).xpath('string()').get()
            item['currency'] = ETH
            item['quality'] = Meteorite
            item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
            card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
            item['image_URL'] = image_URL_base(card_id, 4)

            yield item


def handler():
    process = CrawlerProcess()

    process.crawl(guCardsMeteorite_1_Spider)
    process.crawl(guCardsMeteorite_2_Spider)
    process.crawl(guCardsMeteorite_3_Spider)
    process.crawl(guCardsMeteorite_4_Spider)
    process.crawl(guCardsMeteorite_5_Spider)
    process.crawl(guCardsMeteorite_6_Spider)
    process.crawl(guCardsMeteorite_7_Spider)
    process.crawl(guCardsMeteorite_8_Spider)
    process.crawl(guCardsMeteorite_9_Spider)
    process.crawl(guCardsMeteorite_10_Spider)
    process.crawl(guCardsMeteorite_11_Spider)
    process.crawl(guCardsMeteorite_12_Spider)
    process.crawl(guCardsMeteorite_13_Spider)
    process.crawl(guCardsMeteorite_14_Spider)
    process.crawl(guCardsMeteorite_15_Spider)
    process.crawl(guCardsMeteorite_16_Spider)
    process.crawl(guCardsMeteorite_17_Spider)

    process.start()

