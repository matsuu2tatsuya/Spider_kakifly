# -*- coding: utf-8 -*-
from ..items import TokentroveItem
import re
from selenium.webdriver import Chrome, ChromeOptions
import scrapy
from scrapy.crawler import CrawlerProcess

# 下記の変数は保守性を考えた上です。

def custom_settings(pages):
    return {
        'BOT_NAME': 'tokentrove',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'tokentrove.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['tokentrove.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'tokenTrove.json',
    }

def quality_id(q_id):
    if q_id == '1':
        return 'Diamond'
    elif q_id == '2':
        return 'Gold'
    elif q_id == '3':
        return 'Shadow'
    elif q_id == '4':
        return 'Meteorite'
    else:
        return 'Plain'

def purchase_URL_base(card_id, quality_id):
    return f'https://tokentrove.com/GodsUnchainedCards/{card_id}-{quality_id}'

def image_URL_base(card_id, quality_id):
    return f'https://card.godsunchained.com/?id={card_id}&q={quality_id}&w=256&png=true'

# ここまでが変数ゾーンです。 ここから下は大量のspider作っていきます。



class TokenTrove_1_Spider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']
    custom_settings = custom_settings(1)

    def parse(self, response):
        item = TokentroveItem()
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(20)

        for page in range(1, 16):
            driver.get(f'https://tokentrove.com/GodsUnchainedCards?page={page}&perPage=120')
            driver.find_elements_by_css_selector('div.listing-wrapper')
            response_pages = response.replace(body=driver.page_source)

            for res in response_pages.css('div.listing-wrapper'):
                name = res.css('div.listing-name').xpath('string()').get()
                name2 = re.sub(r',', ' ', name)
                name3 = re.sub(r' $', '', name2)
                name4 = re.sub(r'^ ', '', name3)
                name5 = re.sub(r'  ', ' ', name4)
                item['name'] = re.sub(r"'", "\\'", name5)
                base_price = res.css('div.listing-price').xpath('string()').get()
                item['price'] = re.sub(r'\D*', '', base_price)
                item['currency'] = 'ETH'
                q_id = res.css('composited-card::attr("quality")').get()
                item['quality'] = quality_id(q_id)
                c_id = res.css('composited-card::attr("protoid")').get()
                item['purchase_URL'] = purchase_URL_base(c_id, q_id)
                item['image_URL'] = image_URL_base(c_id, q_id)

                yield item

        driver.quit()

def handler():
    process = CrawlerProcess()
    process.crawl(TokenTrove_1_Spider)
    process.start()

