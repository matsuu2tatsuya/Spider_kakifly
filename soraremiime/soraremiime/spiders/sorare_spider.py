from ..items import SoraremiimeItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class SorareSpider(scrapy.Spider):
    name = 'Sorare_spider'
    allowed_domains = ['miime.io']
    start_urls = ['https://miime.io/assets/12']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'soraremiime.middlewares.soraremiimeSelenium_Middleware': 520,
        },
        'BOT_NAME': 'soraremiime',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'soraremiime.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['soraremiime.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'miime.json',
    }

    def parse(self, response):
        asset_ID = 301000000
        for res in response.css('a.assetCard'):
            if 'miime' in res.css('div.assetCard__priceBox__wrapper__icon > img::attr("src")').get():
                item = SoraremiimeItem()
                base_url = 'https://miime.io/ja/assets/12/0x629a673a8242c2ac4b7b8c5d8735fbeac21a6205/'

                name0 = res.css('div.assetCard__nameBox').xpath('string()').get()
                name = re.sub(r'\n *', "", name0)
                name2 = re.sub(r',', ' ', name)
                name3 = re.sub(r' $', '', name2)
                name4 = re.sub(r'^ ', '', name3)
                name5 = re.sub(r'  ', ' ', name4)
                name6 = re.sub(r'\"', '', name5)
                name7 = re.sub(r"'", "\\'", name6)
                item['player_name'] = re.sub(r" 20.*", "", name7)

                name77 = re.sub(r'.* 2', '', name7)
                item['season'] = '2' + re.sub(r' .*', '', name77)
                name8 = re.sub(r'.*• ', '', name7)
                item['rarity'] = re.sub(r' \d.*', '', name8)
                name10 = re.sub(r'.*Rare ', '', name7)
                item['serial_number'] = re.sub(r'/.*', '', name10)

                price = res.css('div.assetCard__salePrice').xpath('string()').get()
                price2 = re.sub(r'¥', '', price)
                item['price'] = re.sub(r',', '', price2)
                item['currency'] = res.css('div.assetCard__currency').xpath('string()').get()
                if not item['currency']:
                    item['currency'] = 'JPY'
                item['image_URL'] = res.css('div.assetImageWrapper > div > div > img::attr("src")').get()
                purchase = res.css('div.assetCard__tokenId').xpath('string()').get()
                try:
                    purchase2 = re.sub(r'\n \D*', '', purchase)
                except TypeError:
                    pass
                item['purchase_URL'] = base_url + str(purchase2)
                item['asset_ID'] = asset_ID
                asset_ID += 1

                yield item


            elif 'opensea' in res.css('div.assetCard__priceBox__wrapper__icon > img::attr("src")').get():
                item = SoraremiimeItem()
                base_url = 'https://opensea.io/assets/0x629a673a8242c2ac4b7b8c5d8735fbeac21a6205/'
                name0 = res.css('div.assetCard__nameBox').xpath('string()').get()
                name = re.sub(r'\n *', "", name0)
                name2 = re.sub(r',', ' ', name)
                name3 = re.sub(r' $', '', name2)
                name4 = re.sub(r'^ ', '', name3)
                name5 = re.sub(r'  ', ' ', name4)
                name6 = re.sub(r'\"', '', name5)
                name7 = re.sub(r"'", "\\'", name6)
                item['player_name'] = re.sub(r" 20.*", "", name7)

                name77 = re.sub(r'.* 2', '', name7)
                item['season'] = '2' + re.sub(r' .*', '', name77)
                name8 = re.sub(r'.*• ', '', name7)
                item['rarity'] = re.sub(r' \d.*', '', name8)
                name10 = re.sub(r'.*Rare ', '', name7)
                item['serial_number'] = re.sub(r'/.*', '', name10)

                price = res.css('div.assetCard__salePrice').xpath('string()').get()
                price2 = re.sub(r'¥', '', price)
                item['price'] = re.sub(r',', '', price2)
                item['currency'] = res.css('div.assetCard__currency').xpath('string()').get()
                if not item['currency']:
                    item['currency'] = 'JPY'
                item['image_URL'] = res.css('div.assetImageWrapper > div > div > img::attr("src")').get()
                purchase = res.css('div.assetCard__tokenId').xpath('string()').get()
                try:
                    purchase2 = re.sub(r'\n \D*', '', purchase)
                except TypeError:
                    pass
                item['purchase_URL'] = base_url + str(purchase2)
                item['asset_ID'] = asset_ID
                asset_ID += 1

                yield item

def handler():
    process = CrawlerProcess()
    process.crawl(SorareSpider)
    process.start()
