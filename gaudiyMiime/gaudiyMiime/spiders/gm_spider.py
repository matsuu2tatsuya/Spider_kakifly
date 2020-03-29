from ..items import GaudiymiimeItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class gaudiySpider(scrapy.Spider):
    name = 'gaudiy_spider'
    allowed_domains = ['gaudiy.com']
    start_urls = ['https://gaudiy.com/community_details/avJEInz3EXlxNXKMSWxR']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'gaudiyMiime.middlewares.gaudiySelenium_Middleware': 540,
        },
        'BOT_NAME': 'gaudiyMiime',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'gaudiyMiime.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gaudiyMiime.spiders']
    }

    def parse(self, response):
        h = 0
        for res in response.css('button > div > p:nth-child(1)'):
            item = GaudiymiimeItem
            item['name'] = res.get()
            # item['price'] =
            # item['currency'] =
            # item['purchase_URL'] =
            # item['image_URL'] =
            yield item


class miimeSpider(scrapy.Spider):
    name = 'miime_spider'
    allowed_domains = ['miime.io']
    start_urls = ['https://miime.io/assets/2']

    custom_settings = {
        # "DOWNLOADER_MIDDLEWARES": {
        #     'gaudiyMiime.middlewares.miimeSelenium_Middleware': 520,
        # },
        'BOT_NAME': 'gaudiyMiime',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'gaudiyMiime.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gaudiyMiime.spiders']
    }

    def parse(self, response):
        yield


def handler():
    process = CrawlerProcess()
    process.crawl(gaudiySpider)
    # process.crawl(miimeSpider)
    process.start()
