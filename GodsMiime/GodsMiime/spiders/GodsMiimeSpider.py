from ..items import GodsMiimeItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class GodsMiimeSpider(scrapy.Spider):
    name = 'GodsMiime_spider'
    allowed_domains = ['miime.io']
    start_urls = ['https://miime.io/assets/3']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'GodsMiime.middlewares.GodsMiimeSelenium_Middleware': 520,
        },
        'BOT_NAME': 'GodsMiime',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'GodsMiime.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['GodsMiime.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'miime.json',
    }

    def parse(self, response):
        for res in response.css('a.assetCard'):
            if 'miime' in res.css('div.assetCard__priceBox__wrapper__icon > img::attr("src")').get():
                item = GodsMiimeItem()
                base_url = 'https://miime.io/ja/assets/3/0x0e3a2a1f2146d86a604adc220b4967a898d7fe07/'

                name = res.css('div.assetCard__nameBox').xpath('string()').get()
                name2 = re.sub(r'\n *', "\'", name)
                item['name'] = re.sub(r',', ' ', name2)
                price = res.css('div.assetCard__salePrice').xpath('string()').get()
                price2 = re.sub(r'¥', '', price)
                item['price'] = re.sub(r',', '', price2)
                item['currency'] = res.css('div.assetCard__currency').xpath('string()').get()
                if not item['currency']:
                    item['currency'] = 'JPY'
                item['image_URL'] = res.css('div.assetImageWrapper > div > div > img::attr("src")').get()

                if item['image_URL']:
                    if 'diamond' in item['image_URL']:
                        item['quality'] = 'Diamond'
                    if 'gold' in item['image_URL']:
                        item['quality'] = 'Gold'
                    if 'shadow' in item['image_URL']:
                        item['quality'] = 'Shadow'
                    if 'meteorite' in item['image_URL']:
                        item['quality'] = 'Meteorite'

                purchase = res.css('div.assetCard__tokenId').xpath('string()').get()
                try:
                    purchase2 = re.sub(r'\n \D*', '', purchase)
                except TypeError:
                    pass
                item['purchase_URL'] = base_url + str(purchase2)

                yield item


def handler():
    process = CrawlerProcess()
    process.crawl(GodsMiimeSpider)
    process.start()
