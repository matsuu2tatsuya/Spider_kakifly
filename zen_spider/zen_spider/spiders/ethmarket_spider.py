from ..items import EthmarketItem
import re
import scrapy
from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess

"""
イーサマーケット（ETH）のクローラー、スクレイピング。取ってくるItemは、
{ID(auto),name(id or card_name),price(int),currency(ETH),purchase_URL,image_URL}の６つ。
"""

class EthmarketSpider(scrapy.Spider):
    name = 'ethmarket_spider'
    allowed_domains = ['ethmarket.jp']
    start_urls = ['https://ethmarket.jp/']

    custom_settings = {
        "ITEM_PIPELINES": {
            'zen_spider.pipelines.MySQLPipeline': 800,
        },
        "DOWNLOAD_DELAY": 0.5,
        "MYSQL_USER": 'scraper',
        "MYSQL_PASSWORD": 'password',
    }

    def parse(self, response):

        for res in response.xpath('//table[@class="cardBlock"]'):

            eth_items = EthmarketItem()
            base_url = 'https://ethmarket.jp/'

            eth_items['ID'] = None

            card_name_path = res.css('img[src$="png"]::attr("src")').get()   # →名前
            card_name = re.sub(r'/Content/CardImage/', '', card_name_path)
            eth_items['name'] = re.sub(r'.png', '', card_name)

            try:
                eth_items['price'] = res.css('[class=buyButton] > a > font').xpath('string()').re(r'.*\d+')[0]  # →価格ETH
            except IndexError:
                raise DropItem('OUT OF STOCK')

            eth_items['currency'] = 'ETH'

            eth_buy_url = res.css('a::attr("href")').re(r'\d+$')[0]   # purchase_URL
            eth_items['buy_transaction_URL'] = base_url + '/buytransactions/create?cardId=' + eth_buy_url


            eth_img_url = res.css('img[src$="png"]::attr("src")').get()  # →イメージファイルURL
            eth_items['image_URL'] = base_url + eth_img_url


            yield eth_items


#process = CrawlerProcess()
#process.crawl(EthmarketSpider)

#process.start()
