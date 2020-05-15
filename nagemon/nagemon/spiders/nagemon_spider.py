# -*- coding: utf-8 -*-
from ..items import NagemonItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class NagemonSpiderSpider(scrapy.Spider):
    name = 'nagemon_spider'
    allowed_domains = ['www.nagemon.com']
    start_urls = ['https://www.nagemon.com/assets/sell']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'nagemon.middlewares.nagemonSelenium_Middleware': 540,
        },
        'BOT_NAME': 'nagemon',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'nagemon.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['nagemon.spiders'],
        'FEED_FORMAT': 'xml',
        'FEED_URI': 'nagemon.xml',
    }

    def parse(self, response):
        for res in response.css('div.game-card'):
            item = NagemonItem()
            base_url = 'https://www.nagemon.com'

            base_name = res.css('p.name-ai-game').xpath('string()').get()
            item['name'] = re.sub(r'\s\D{2,12}$', '', base_name)

            base_price = res.css('p.ethFavTxt').get()
            base_price2 = re.sub(r'^<\D*>', '', base_price)
            item['price'] = re.sub(r'\D*<span\D*.*p>', '', base_price2)

            base_currency = re.sub(r'^<\D*>\d*.\d*\s*', '', base_price)
            item['currency'] = re.sub(r'\d*<span\D*.*p>', '', base_currency)

            base_quality = re.findall(r'\s\D{2,9}$', base_name)[0]
            item['quality'] = re.sub(r'\s', '', base_quality)

            item['purchase_URL'] = base_url + res.css('a.cursor-pointer::attr("href")').get()
            item['image_URL'] = res.css('img.img-game::attr("src")').get()

            yield item



def handler():
    process = CrawlerProcess()
    process.crawl(NagemonSpiderSpider)
    process.start()

