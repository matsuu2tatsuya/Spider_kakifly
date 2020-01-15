from ..items import EthmarketItem_JPY
import re
import scrapy
from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess

"""
イーサマーケット（JPY）のクローラー、スクレイピング。取ってくるItemは、
{ID(auto),name(id or card_name),price(int),currency(JPY),purchase_URL,image_URL}の６つ。
"""

class EthmarketSpider_JPY(scrapy.Spider):
    name = 'ethmarket_jp_spider'
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

            eth_items_jp = EthmarketItem_JPY()
            base_url = 'https://ethmarket.jp/'

            eth_items_jp['ID'] = None

            card_name_path = res.css('img[src$="png"]::attr("src")').get()   # →名前
            card_name = re.sub(r'/Content/CardImage/', '', card_name_path)
            eth_items_jp['name'] = re.sub(r'.png', '', card_name)

            try:
                res.css('[class=buyButton] > a > font').xpath('string()').re(r'.*\d+')[0]  # →売り切れがあっても続行
            except IndexError:
                raise DropItem('OUT OF STOCK')

            eth_items_jp['price'] = res.css('[class=buyButton] > a > font').xpath('string()').re(r'.*\d+')[1]  # →価格JPY

            eth_items_jp['currency'] = 'JPY'

            eth_JPY_url = res.css('a[href$="JPY"]::attr("href")').get()  # JRYの買取URL
            eth_items_jp['buy_transaction_URL'] = base_url + eth_JPY_url


            eth_img_url = res.css('img[src$="png"]::attr("src")').get()  # →イメージファイルURL
            eth_items_jp['image_URL'] = base_url + eth_img_url


            yield eth_items_jp


#process = CrawlerProcess()
#process.crawl(EthmarketSpider_JPY)

#process.start()