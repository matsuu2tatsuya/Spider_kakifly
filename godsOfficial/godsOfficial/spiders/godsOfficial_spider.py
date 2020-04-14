# -*- coding: utf-8 -*-
from ..items import GodsofficialItem
import re
import requests
import json
import scrapy
from scrapy.crawler import CrawlerProcess


class GodsofficialSpider(scrapy.Spider):
    name = 'godsOfficial_spider'
    allowed_domains = ['godsunchained.com']
    start_urls = ['https://godsunchained.com/marketplace/search?groupby=name&sortby=timestamp&orderby=desc&currentpage=1&perpage=1800']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'godsOfficial.middlewares.godsOfficial_Selenium_Middleware': 540,
        },
        'BOT_NAME': 'godsOfficial',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'godsOfficial.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['godsOfficial.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'godsOfficial.json',
    }

    def parse(self, response):
        for res in response.css('div.assets__cardItem'):
            item = GodsofficialItem()
            base_url = res.css('img.cardImagery__img::attr("srcset")').get()

            def base_purchase_url(asset_id, quality, contract):
                return f'https://godsunchained.com/marketplace/search/(asset:details/{asset_id}/{quality}/{contract})'

            base_name = re.sub(r'^.*id=', '', base_url)
            name_id = re.sub(r'&.*$', '', base_name)
            # gods_api_url = f'https://api.godsunchained.com/v0/proto/{name_id}'
            # api_response = requests.get(gods_api_url)
            # jsonData = api_response.json()
            item['name'] = name_id

            # base_price = res.css('p.ethFavTxt').get()
            # base_price2 = re.sub(r'^<\D*>', '', base_price)
            item['price'] = res.css('gu-heading-text.cardItemFooter__price').xpath('string()').get()

            item['currency'] = 'ETH'

            base_quality = re.sub(r'^.*q=', '', base_url)
            quality_id = re.sub(r'&.*$', '', base_quality)
            if quality_id == '1':
                item['quality'] = 'Diamond'
            elif quality_id == '2':
                item['quality'] = 'Gold'
            elif quality_id == '3':
                item['quality'] = 'Shadow'
            elif quality_id == '4':
                item['quality'] = 'Meteorite'
            else:
                item['quality'] = 'Plain'

            item['purchase_URL'] = base_purchase_url(name_id, quality_id, 'your_contract_number')
            item['image_URL'] = base_url

            yield item




def handler():
    process = CrawlerProcess()
    process.crawl(GodsofficialSpider)
    process.start()
