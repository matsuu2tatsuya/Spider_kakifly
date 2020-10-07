# -*- coding: utf-8 -*-
from ..items import CryspeSoldoutItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class MagiSoldoutSpider(scrapy.Spider):
    name = 'magi_soldout__spider'
    allowed_domains = ['magi.camp']
    start_urls = ['https://magi.camp/items/search?utf8=%E2%9C%93&forms_search_items%5Bkeyword%5D=&forms_search_items%5Bcategory_id%5D=100009&forms_search_items%5Btag_id%5D=&forms_search_items%5Bfrom_price%5D=&forms_search_items%5Bto_price%5D=&forms_search_items%5Bquality%5D=&forms_search_items%5Bstatus%5D=sold_out&forms_search_items%5Bsort%5D=&forms_search_items%5Bpage%5D=1&commit=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B']
    custom_settings = {
        "DOWNLOAD_DELAY": 1.0,
        "CONCURRENT_REQUESTS": 32,
        "MYSQL_USER": 'scraper',
        "MYSQL_PASSWORD": 'password',
        "FEED_EXPORT_ENCODING": 'utf-8',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'magi_soldout.json',
    }

    def parse(self, response):
        for res in response.xpath('//div[@class="item-list__box"]'):
            magi_items = CryspeSoldoutItem()
            base_url = 'https://magi.camp/'

            card_name = res.css('[class=item-list__item-name]').xpath('string()').get()      # →名前
            magi_items['name'] = re.sub(r' ', '', card_name)

            jpy_buy_price_path = res.css('[class=item-list__price-box--price]').xpath('string()').re_first(r'.*\d+')  # →価格JPY
            jpy_buy_price = re.sub(r'¥ ', '', jpy_buy_price_path)
            magi_items['price'] = re.sub(r',', '', jpy_buy_price)

            magi_items['currency'] = 'JPY'

            eth_buy_url = res.css('a::attr("href")').re_first(r'/items/\d+$')   # 買取URL
            magi_items['purchase_URL'] = base_url + eth_buy_url

            magi_items['image_URL'] = res.css('img::attr("data-src")').get()  # →イメージファイルURL

            yield magi_items

        next_page = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, callback=self.parse)


class CryspeSoldoutSpider(scrapy.Spider):
    name = 'cryspe_soldout_spider'
    allowed_domains = ['cryptospells.jp/trades']
    start_urls = ['https://cryptospells.jp/trades/']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'cryspe_soldout.middlewares.cryspe_SeleniumMiddleware': 543,
        },
        "DOWNLOAD_DELAY": 1.0,
        "CONCURRENT_REQUESTS": 32,
        "MYSQL_USER": 'scraper',
        "MYSQL_PASSWORD": 'password',
        "FEED_EXPORT_ENCODING": 'utf-8',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'cryspe_soldout.json',
    }


    def parse(self, response):
        for res in response.xpath('//div[@class="col-4 col-sm-2 col-sm-2--half col-card"]'):
            if res.css('.card-image-black-filter'):
                cryspe_items = CryspeSoldoutItem()
                base_URL = 'https://cryptospells.jp'

                ID_path = res.css('[class="serial-number serial-number-user-img-wrapper"]').xpath('string()').get()
                ID_path2 = re.sub(r'# .', '', ID_path)
                cryspe_items['name'] = re.sub(r' .*', '', ID_path2)

                SPL_path = res.css('[class="price"]').xpath('string()').get()
                SPL_path2 = re.sub(r' SPL', '', SPL_path)
                cryspe_items['price'] = re.sub(r',', '', SPL_path2)

                cryspe_items['currency'] = 'SPL'

                cryspe_items['purchase_URL'] = base_URL + res.css('a::attr("href")').re_first(r'/trades/\d+$')

                cryspe_items['image_URL'] = res.css('img[src$="png"]::attr("src")').get()

                yield cryspe_items
            else:
                pass


process = CrawlerProcess()
process.crawl(MagiSoldoutSpider)
# process.crawl(CryspeSoldoutSpider)

process.start()
