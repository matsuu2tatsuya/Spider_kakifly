from ..items import GucardsnagemonItem
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
            'gucardsNagemon.middlewares.guCardsSelenium_Middleware': 520,
        },
        'BOT_NAME': 'gucardsNagemon',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'gucardsNagemon.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gucardsNagemon.spiders'],
        # 'FEED_FORMAT': 'json',
        # 'FEED_URI': 'gaudiy.json',
    }

    def parse(self, response):
        for res in response.css('div.js-card-with-trading-buttons'):
            item = GucardsnagemonItem()
            item['name'] = res.css('div.card-name-cell > span').xpath('string()').get()
            yield item


class nagemonSpider(scrapy.Spider):
    name = 'nagemon_spider'
    allowed_domains = ['miime.io']
    start_urls = ['https://miime.io/assets/2']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'gaudiyMiime.middlewares.miimeSelenium_Middleware': 520,
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
        'SPIDER_MODULES': ['gaudiyMiime.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'miime.json',
    }

    def parse(self, response):
        for res in response.css('a.assetCard'):
            item = GaudiymiimeItem()
            base_url = 'https://miime.io/assets/2/0x67cbbb366a51fff9ad869d027e496ba49f5f6d55/'

            name = res.css('div.assetCard__nameBox').xpath('string()').get()
            item['name'] = re.sub(r'\n *', '', name)
            item['price'] = res.css('div.assetCard__salePrice').xpath('string()').get()
            item['currency'] = res.css('div.assetCard__currency').xpath('string()').get()
            item['image_URL'] = res.css('div.assetImageWrapper > div > div > img::attr("src")').get()
            purchase = res.css('div.assetCard__tokenId').xpath('string()').get()
            try:
                purchase2 = re.sub(r'\n \D*', '', purchase)
            except TypeError:
                pass
            item['purchase_URL'] = base_url + str(purchase2)

            yield item

# def handler():
#     process = CrawlerProcess()
#     process.crawl(gaudiySpider)
#     process.crawl(miimeSpider)
#     process.start()
