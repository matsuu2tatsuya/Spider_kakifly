from ..items import GuCardsItem
import re
import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess


class guCardsSpider(scrapy.Spider):
    name = 'guCards_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['https://gu.cards/?marketplace=with_listings']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'gu_cards.middlewares.guCardsSelenium_Middleware': 520,
        },
    }

    def parse(self, response):
        for res in response.css('div.js-card-with-trading-buttons'):
            item = GuCardsItem()
            item['name'] = res.css('div.card-name-cell > span').xpath('string()').get()

            yield item
