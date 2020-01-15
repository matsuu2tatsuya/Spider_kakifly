from ..items import Cryptospells_Item
import re
import scrapy
from scrapy.crawler import CrawlerProcess

"""
クリプトスペルズ内マーケット（SPL）のクローラー、スクレイピング。取ってくるItemは、
{ID(auto),name(id or card_name),price(int),currency(SPL),purchase_URL,image_URL}の６つ。
"""

class cryspe_selenium(scrapy.Spider):
    name = 'cryspe_Selenium'
    allowed_domains = ['cryptospells.jp/trades']
    start_urls = ['https://cryptospells.jp/trades/']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'zen_spider.middlewares.cryspe_SeleniumMiddleware': 543,
        },
        "ITEM_PIPELINES": {
            'zen_spider.pipelines.MySQLPipeline': 800,
        },
        "DOWNLOAD_DELAY": 0.5,
        "MYSQL_USER": 'scraper',
        "MYSQL_PASSWORD": 'password',
    }


    def parse(self, response):
        for res in response.xpath('//div[@class="col-4 col-sm-2 col-sm-2--half col-card"]'):
            cryspe_items = Cryptospells_Item()
            base_URL = 'https://cryptospells.jp'

            cryspe_items['ID'] = None

            ID_path = res.css('[class="serial-number serial-number-user-img-wrapper"]').xpath('string()').get()
            ID_path2 = re.sub(r'# ', '', ID_path)
            cryspe_items['name'] = re.sub(r' ', '', ID_path2)

            SPL_path = res.css('[class="price"]').xpath('string()').get()
            SPL_path2 = re.sub(r' SPL', '', SPL_path)
            cryspe_items['price'] = re.sub(r',', '', SPL_path2)

            cryspe_items['currency'] = 'SPL'

            cryspe_items['buy_transaction_URL'] = base_URL + res.css('a::attr("href")').re_first(r'/trades/\d+$')

            cryspe_items['image_URL'] = res.css('img[src$="png"]::attr("src")').get()

            yield cryspe_items


process = CrawlerProcess()
process.crawl(cryspe_selenium)

process.start()