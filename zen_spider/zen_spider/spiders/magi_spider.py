from ..items import MagiItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess

"""
Magi（JPY）のクローラー、スクレイピング。取ってくるItemは、
{ID(auto),name(id or card_name),price(int),currency(JPY),purchase_URL,image_URL}の６つ。
"""

class MagiSpider(scrapy.Spider):
    name = 'magi_spider'
    allowed_domains = ['magi.camp']
    start_urls = ['https://magi.camp/items/search?utf8=%E2%9C%93&forms_search_items%5Bcategory_id%5D=100009&forms_search_items%5Bstatus%5D=presented&forms_search_items%5Bpage%5D=1&commit=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B']

    custom_settings = {
        "ITEM_PIPELINES": {
            'zen_spider.pipelines.MySQLPipeline': 800,
        },
        "DOWNLOAD_DELAY": 0.5,
        "MYSQL_USER": 'scraper',
        "MYSQL_PASSWORD": 'password',
    }

    def parse(self, response):

        for res in response.xpath('//div[@class="item-list__box"]'):

            magi_items = MagiItem()
            base_url = 'https://magi.camp/'

            magi_items['ID'] = None

            card_name = res.css('[class=item-list__item-name]').xpath('string()').get()      # →名前
            magi_items['name'] = re.sub(r' ', '', card_name)

            jpy_buy_price_path = res.css('[class=item-list__price-box--price]').xpath('string()').re_first(r'.*\d+')  # →価格JPY
            jpy_buy_price = re.sub(r'¥ ', '', jpy_buy_price_path)
            magi_items['price'] = re.sub(r',', '', jpy_buy_price)

            magi_items['currency'] = 'JPY'

            eth_buy_url = res.css('a::attr("href")').re_first(r'/items/\d+$')   # 買取URL
            magi_items['buy_transaction_URL'] = base_url + eth_buy_url

            magi_items['image_URL'] = res.css('img[data-src$="jpg"]::attr("data-src")').get()  # →イメージファイルURL

            yield magi_items

        next_page = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, callback=self.parse)


#process = CrawlerProcess()
#process.crawl(MagiSpider)

#process.start()
