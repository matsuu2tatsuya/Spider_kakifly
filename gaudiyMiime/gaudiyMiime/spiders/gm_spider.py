from ..items import GaudiymiimeItem
import re
import scrapy
from scrapy.crawler import CrawlerProcess


class gaudiySpider(scrapy.Spider):
    name = 'gaudiy_spider'
    allowed_domains = ['gaudiy.com']
    start_urls = ['https://gaudiy.com/community_details/avJEInz3EXlxNXKMSWxR']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'gaudiyMiime.middlewares.gaudiySelenium_Middleware': 540,
        },
        'BOT_NAME': 'gaudiyMiime',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'gaudiyMiime.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gaudiyMiime.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'gaudiy.json',
    }

    def parse(self, response):
        item = GaudiymiimeItem()
        for res in response.css('div.react-swipeable-view-container > div > div > div > div > div > div > div > button.MuiButtonBase-root'):
            if res.xpath('string()').get() == 'アセット一覧':
                yield
            elif res.xpath('string()').get() == 'すべての出品':
                yield
            elif res.xpath('string()').get() == 'オークション':
                yield
            elif res.xpath('string()').get() == 'レンタル':
                yield
            else:
                name = res.xpath('string()').get()
                name2 = re.sub(r'出品\d.*', '', name)
                name3 = re.sub(r' ', '', name2)
                name4 = re.sub(r'\u3000', '', name3)
                item['name'] = re.sub(r'\t', '', name4)

                item['currency'] = 'ETH'
                price = res.css('div > p:nth-child(3)').xpath('string()').get()
                item['price'] = re.sub(r'ETH~', '', str(price))
                if re.sub(r'ETH~', '', str(price)) == '出品待ち':
                    break

                item['image_URL'] = res.css('div > div > span > img::attr("src")').get()

                yield item


class miimeSpider(scrapy.Spider):
    name = 'miime_spider'
    allowed_domains = ['miime.io']
    start_urls = ['https://miime.io/assets/2']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'gaudiyMiime.middlewares.miimeSelenium_Middleware': 520,
        },
        'BOT_NAME': 'gaudiyMiime',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'gaudiyMiime.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gaudiyMiime.spiders'],
        'FEED_FORMAT': 'json',
        'FEED_URI': 'miime.json',
    }

    def parse(self, response):
        for res in response.css('a.assetCard'):
            item = GaudiymiimeItem()
            base_url = 'https://miime.io/assets/2/0x67cbbb366a51fff9ad869d027e496ba49f5f6d55/'

            name = res.css('div.assetCard__nameBox').xpath('string()').get()
            item['name'] = re.sub(r'\n *', '', name)
            item['price'] = res.css('div.assetCard__salePrice').xpath('string()').get()
            item['currency'] = res.css('div.assetCard__currency').xpath('string()').get()
            item['image_URL'] = res.css('div.assetImageWrapper > div > div > img::attr("src")').get()
            purchase = res.css('div.assetCard__tokenId').xpath('string()').get()
            try:
                purchase2 = re.sub(r'\n \D*', '', purchase)
            except TypeError:
                pass
            item['purchase_URL'] = base_url + str(purchase2)

            yield item


def handler():
    process = CrawlerProcess()
    process.crawl(gaudiySpider)
    # process.crawl(miimeSpider)
    process.start()
