# -*- coding: utf-8 -*-
from ..items import GodsofficialItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class GodsofficialSpider(scrapy.Spider):
    name = 'godsOfficial_spider'
    allowed_domains = ['godsunchained.com']
    start_urls = ['https://godsunchained.com/marketplace/search?groupby=name&sortby=timestamp&orderby=desc&currentpage=1&perpage=100']
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
        'FEED_FORMAT': 'csv',
        'FEED_URI': '07.csv',
    }

    def parse(self, response):
        asset_ID = 201000000
        for res in response.css('div.assets__cardItem'):
            item = GodsofficialItem()
            base_url = str(res.css('img.assetImagery__img::attr("srcset")').get())

            def base_purchase_url(asset_id, quality, contract):
                return f'https://godsunchained.com/marketplace/search/(asset:details/{asset_id}/{quality}/{contract}/card)'

            base_name = re.sub(r'^.*id=', '', base_url)
            name_id = re.sub(r'&.*$', '', base_name)
            # gods_api_url = f'https://api.godsunchained.com/v0/proto/{name_id}'
            # api_response = requests.get(gods_api_url)
            # jsonData = api_response.json()
            name = res.css('gu-simple-text.cardItemFooter__fromText').xpath('string()').get()
            name2 = re.sub(r',', ' ', name)
            name3 = re.sub(r' $', '', name2)
            name4 = re.sub(r'^ ', '', name3)
            name5 = re.sub(r'  ', ' ', name4)
            item['name'] = re.sub(r"'", "\\'", name5)

            # base_price = res.css('p.ethFavTxt').get()
            # base_price2 = re.sub(r'^<\D*>', '', base_price)
            get_price = res.css('gu-heading-text.cardItemFooter__price').xpath('string()').get()
            if get_price == ' ':
                item['price'] = 0
            else:
                item['price'] = get_price

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
            item['image_URL'] = re.sub(r'w=128', 'w=512', base_url)
            item['asset_ID'] = asset_ID
            asset_ID += 1

            yield item





def handler():
    process = CrawlerProcess()
    process.crawl(GodsofficialSpider)
    process.start()
