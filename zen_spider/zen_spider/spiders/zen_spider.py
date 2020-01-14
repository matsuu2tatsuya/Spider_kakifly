# -*- coding: utf-8 -*-
from ..items import EthmarketItem, MagiItem, Cryptospells_Item, spider_DEX_Item
import re
import scrapy
from scrapy_splash import SplashRequest
from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess

"""
spider crawl 引数 -o {name}.json
実行時の引数。:ethmarket_spider, :magi_spider, :cryspe_splash, :DEX_spider
"""

"""
MYSQL -> items テーブルに入れるデータ。
`ID`,`name`,`price_ETH`, `price_SPL`,`price_JPY`,`buy_transaction_URL`,
`sell_transaction_URL_ETH`,`buy_transaction_URL_JPY`,`image_URL

計９個 primary_key は buy_transaction_URL
"""


class EthmarketSpider(scrapy.Spider):
    name = 'ethmarket_spider'
    allowed_domains = ['ethmarket.jp']
    start_urls = ['https://ethmarket.jp/']

    def parse(self, response):

        for res in response.xpath('//table[@class="cardBlock"]'):

            eth_items = EthmarketItem()
            base_url = 'https://ethmarket.jp/'

            eth_items['ID'] = None

            card_name_path = res.css('img[src$="png"]::attr("src")').get()   # →名前
            card_name = re.sub(r'/Content/CardImage/', '', card_name_path)
            eth_items['name'] = re.sub(r'.png', '', card_name)

            try:
                eth_items['price_ETH'] = res.css('[class=buyButton] > a > font').xpath('string()').re(r'.*\d+')[0]  # →価格ETH
            except IndexError:
                raise DropItem('OUT OF STOCK')

            eth_items['price_SPL'] = None
            eth_items['price_JPY'] = res.css('[class=buyButton] > a > font').xpath('string()').re(r'.*\d+')[1]  # →価格JPY

            eth_buy_url = res.css('a::attr("href")').re(r'\d+$')[0]   # 買取URL
            eth_items['buy_transaction_URL'] = base_url + '/buytransactions/create?cardId=' + eth_buy_url

            eth_sell_url = res.css('a[id^=sellAction]::attr("href")').get()  # 売却URL
            eth_items['sell_transaction_URL_ETH'] = base_url + eth_sell_url

            eth_JPY_url = res.css('a[href$="JPY"]::attr("href")').get()  # JRYの買取URL
            eth_items['buy_transaction_URL_JPY'] = base_url + eth_JPY_url


            eth_img_url = res.css('img[src$="png"]::attr("src")').get()  # →イメージファイルURL
            eth_items['image_URL'] = base_url + eth_img_url


            yield eth_items


class MagiSpider(scrapy.Spider):
    name = 'magi_spider'
    allowed_domains = ['magi.camp']
    start_urls = ['https://magi.camp/items/search?utf8=%E2%9C%93&forms_search_items%5Bcategory_id%5D=100009&forms_search_items%5Bstatus%5D=presented&forms_search_items%5Bpage%5D=1&commit=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B']

    def parse(self, response):

        for res in response.xpath('//div[@class="item-list__box"]'):

            magi_items = MagiItem()
            base_url = 'https://magi.camp/'

            magi_items['ID'] = None

            card_name = res.css('[class=item-list__item-name]').xpath('string()').get()      # →名前
            magi_items['name'] = re.sub(r' ', '', card_name)

            magi_items['price_ETH'] = None
            magi_items['price_SPL'] = None

            jpy_buy_price_path = res.css('[class=item-list__price-box--price]').xpath('string()').re_first(r'.*\d+')  # →価格JPY
            jpy_buy_price = re.sub(r'¥ ', '', jpy_buy_price_path)
            magi_items['price_JPY'] = re.sub(r',', '', jpy_buy_price)

            eth_buy_url = res.css('a::attr("href")').re_first(r'/items/\d+$')   # 買取URL
            magi_items['buy_transaction_URL'] = base_url + eth_buy_url

            magi_items['sell_transaction_URL_ETH'] = None
            magi_items['buy_transaction_URL_JPY'] = None

            magi_items['image_URL'] = res.css('img[data-src$="jpg"]::attr("data-src")').get()  # →イメージファイルURL

            yield magi_items

        next_page = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, callback=self.parse)



class CryspeSpider(scrapy.Spider):
    name = 'cryspe_splash'
    allowed_domains = ['cryptospells.jp/trades']
    start_urls = ['https://cryptospells.jp/trades/']


    def start_requests(self):
        script = """
        function main(splash, args)
            local num_scrolls = 25
            local scroll_delay = 0.5
            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            assert(splash:go(splash.args.url))
            assert(splash:wait(0.5)) 
            local area = splash:select('.checkmark')
            area:click()
            assert(splash:wait(0.5)) 

        for _ = 1, num_scrolls do
                scroll_to(0, get_body_height())
                splash:wait(scroll_delay)
            end 
            return {
                html = splash:html(),
                png = splash:png(),
                har = splash:har(),
            }
        end
                """
        yield SplashRequest(url='https://cryptospells.jp/trades/', callback=self.parse, endpoint='execute',
                            args={'lua_source': script})

        # yield SplashRequest(url=url, callback=self.parse, args={"wait": 3})

    def parse(self, response):
        for res in response.xpath('//div[@class="col-4 col-sm-2 col-sm-2--half col-card"]'):
            cryspe_items = Cryptospells_Item()
            base_URL = 'https://cryptospells.jp'

            # cryspe_items['name'] = res.css('[class=mycard-header__name]').xpath('string()').get().strip()
            cryspe_items['name'] = None

            ID_path = res.css('[class="serial-number serial-number-user-img-wrapper"]').xpath('string()').get()
            ID_path2 = re.sub(r'# ', '', ID_path)
            cryspe_items['ID'] = re.sub(r' ', '', ID_path2)

            cryspe_items['price_ETH'] = None
            SPL_path = res.css('[class="price"]').xpath('string()').get()
            SPL_path2 = re.sub(r' SPL', '', SPL_path)
            cryspe_items['price_SPL'] = re.sub(r',', '', SPL_path2)
            cryspe_items['price_JPY'] = None

            cryspe_items['buy_transaction_URL'] = base_URL + res.css('a::attr("href")').re_first(r'/trades/\d+$')
            cryspe_items['sell_transaction_URL_ETH'] = None
            cryspe_items['buy_transaction_URL_JPY'] = None

            cryspe_items['image_URL'] = res.css('img[src$="png"]::attr("src")').get()

            yield cryspe_items


class cryspe_selenium(scrapy.Spider):
    name = 'cryspe_Selenium'
    allowed_domains = ['spiderdex.com/assets/5d35228f74ba04002ac53d9c']
    start_urls = ['https://www.spiderdex.com/assets/5d35228f74ba04002ac53d9c']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'zen_spider.middlewares.cryspe_SeleniumMiddleware': 543,
        },
        "DOWNLOAD_DELAY": 0.5,
    }

    def parse(self, response):
        for res in response.xpath('//div[@class="col-4 col-sm-2 col-sm-2--half col-card"]'):
            cryspe_items = Cryptospells_Item()
            base_URL = 'https://cryptospells.jp'

            # cryspe_items['name'] = res.css('[class=mycard-header__name]').xpath('string()').get().strip()
            cryspe_items['name'] = None

            ID_path = res.css('[class="serial-number serial-number-user-img-wrapper"]').xpath('string()').get()
            ID_path2 = re.sub(r'# ', '', ID_path)
            cryspe_items['ID'] = re.sub(r' ', '', ID_path2)

            cryspe_items['price_ETH'] = None
            SPL_path = res.css('[class="price"]').xpath('string()').get()
            SPL_path2 = re.sub(r' SPL', '', SPL_path)
            cryspe_items['price_SPL'] = re.sub(r',', '', SPL_path2)
            cryspe_items['price_JPY'] = None

            cryspe_items['buy_transaction_URL'] = base_URL + res.css('a::attr("href")').re_first(r'/trades/\d+$')
            cryspe_items['sell_transaction_URL_ETH'] = None
            cryspe_items['buy_transaction_URL_JPY'] = None

            cryspe_items['image_URL'] = res.css('img[src$="png"]::attr("src")').get()

            yield cryspe_items



class DEX_Spider(scrapy.Spider):
    name = 'DEX_spider'
    allowed_domains = ['spiderdex.com/assets/5d35228f74ba04002ac53d9c']
    start_urls = ['https://www.spiderdex.com/assets/5d35228f74ba04002ac53d9c']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'zen_spider.middlewares.SeleniumMiddleware': 543,
        },
        "DOWNLOAD_DELAY": 0.5,
    }

    def parse(self, response):
        dex_item = spider_DEX_Item()

        name_ID = response.css('span.assetdetailname').xpath('string()').get()

        dex_item['ID'] = re.sub(r'\D+', '', name_ID)
        dex_item['name'] = re.sub(r' #\d+', '', name_ID)

        price_path = response.css('div.assetdetailprice').xpath('string()').get()
        price_path2 = re.sub(r'Price:', '', price_path)
        price_path3 = re.sub(r'\xa0', '', price_path2)
        dex_item['price_ETH'] = re.sub(r'ETH', '', price_path3)
        dex_item['price_SPL'] = None
        dex_item['price_JPY'] = None

        dex_item['buy_transaction_URL'] = response.url
        dex_item['sell_transaction_URL_ETH'] = None
        dex_item['buy_transaction_URL_JPY'] = None

        dex_item['image_URL'] = response.css('img[src$="png"]::attr("src")').get()

        return dex_item





