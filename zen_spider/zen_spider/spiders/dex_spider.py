from ..items import Spider_DEX_Item
import re
import scrapy
from scrapy.crawler import CrawlerProcess

"""
spider_DEX （ETH）のクローラー、スクレイピング。取ってくるItemは、
{ID(auto),name(id or card_name),price(int),currency(ETH),purchase_URL,image_URL}の６つ。
"""

class DEX_Spider(scrapy.Spider):
    name = 'DEX_spider'
    allowed_domains = ['spiderdex.com/assets/5d35228f74ba04002ac53d9c']
    start_urls = ['https://www.spiderdex.com/assets/5d35228f74ba04002ac53d9c']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'zen_spider.middlewares.SeleniumMiddleware': 543,
        },
        "ITEM_PIPELINES": {
            'zen_spider.pipelines.MySQLPipeline': 800,
        },
        "DOWNLOAD_DELAY": 1.0,
        "MYSQL_USER": 'scraper',
        "MYSQL_PASSWORD": 'password',
    }

    def parse(self, response):
        dex_items = Spider_DEX_Item()

        name_ID = response.css('span.assetdetailname').xpath('string()').get()

        dex_items['ID'] = None
        dex_items['name'] = re.sub(r'\D+', '', name_ID)

        price_path = response.css('div.assetdetailprice').xpath('string()').get()
        price_path2 = re.sub(r'Price:', '', price_path)
        price_path3 = re.sub(r'\xa0', '', price_path2)
        dex_items['price'] = re.sub(r'ETH', '', price_path3)

        dex_items['currency'] = 'ETH'

        dex_items['buy_transaction_URL'] = response.url

        dex_items['image_URL'] = response.css('img[src$="png"]::attr("src")').get()

        return dex_items


process = CrawlerProcess()
process.crawl(DEX_Spider)

process.start()