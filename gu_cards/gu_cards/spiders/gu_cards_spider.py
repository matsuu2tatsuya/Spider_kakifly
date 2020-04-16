from ..items import GuCardsItem
import re
from selenium.webdriver import Chrome, ChromeOptions
import scrapy
from scrapy.crawler import CrawlerProcess


# 下記の変数は保守性を考えた上です。
all_cards = 'div.js-card-with-trading-buttons'
name_base = 'div.card-name-cell > span'
price_base = 'button.js-buy-button > span'
ETH = 'ETH'
Shadow = 'Shadow'        # quality_id = 3
Gold = 'Gold'            # quality_id = 2
Diamond = 'Diamond'      # quality_id = 1
base_url = 'https://gu.cards/'
purchase_URL_base = 'a.js-card-link::attr("href")'

def custom_settings(quality):
    return {
        'BOT_NAME': 'gu_cards',
        'NEWSPIDER_MODULE': 'gu_cards.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['gu_cards.spiders'],
        'USER_AGENT': 'gu_cards (+http://www.yourdomain.com)',
        'CONCURRENT_REQUESTS': 16,
        'DOWNLOAD_DELAY': 1,
        "FEED_EXPORT_ENCODING": 'utf-8',
        "FEED_FORMAT": 'json',
        "FEED_URI": f'guCards{quality}.json',
    }

def image_URL_base(card_id, quality_id):
    return f'https://card.godsunchained.com/?id={card_id}&q={quality_id}&w=256&png=true'

# ここまでが変数ゾーンです。 ここから下は大量のspider作っていきます。

# Shadow
class guCardsShadow_Spider(scrapy.Spider):
    name = 'guCardsShadow_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['http://example.com/']
    custom_settings = custom_settings(Shadow)

    def parse(self, response):
        item = GuCardsItem()
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(20)

        for page in range(1, 10):
            driver.get(f'https://gu.cards/?marketplace=with_listings&page={page}&quality_shadow=on')
            driver.find_elements_by_css_selector('div.js-card-with-trading-buttons')
            response_pages = response.replace(body=driver.page_source)

            for res in response_pages.css(all_cards):
                item['name'] = res.css(name_base).xpath('string()').get()
                item['price'] = res.css(price_base).xpath('string()').get()
                item['currency'] = ETH
                item['quality'] = Shadow
                item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
                card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
                item['image_URL'] = image_URL_base(card_id, 3)

                yield item

            try:
                driver.implicitly_wait(3)
                driver.find_element_by_css_selector('i.fa-caret-right')
            except Exception:
                return

        driver.quit()

# Gold
class guCardsGold_Spider(scrapy.Spider):
    name = 'guCardsGold_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['http://example.com/']
    custom_settings = custom_settings(Gold)

    def parse(self, response):
        item = GuCardsItem()
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(20)

        for page in range(1, 5):
            driver.get(f'https://gu.cards/?marketplace=with_listings&page={page}&quality_gold=on')
            driver.find_elements_by_css_selector('div.js-card-with-trading-buttons')
            response_pages = response.replace(body=driver.page_source)

            for res in response_pages.css(all_cards):
                item['name'] = res.css(name_base).xpath('string()').get()
                item['price'] = res.css(price_base).xpath('string()').get()
                item['currency'] = ETH
                item['quality'] = Gold
                item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
                card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
                item['image_URL'] = image_URL_base(card_id, 2)

                yield item

            try:
                driver.implicitly_wait(3)
                driver.find_element_by_css_selector('i.fa-caret-right')
            except Exception:
                return

        driver.quit()


# Diamond
class guCardsDiamond_Spider(scrapy.Spider):
    name = 'guCardsDiamond_spider'
    allowed_domains = ['gu.cards']
    start_urls = ['http://example.com/']
    custom_settings = custom_settings(Diamond)

    def parse(self, response):
        item = GuCardsItem()
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(20)

        for page in range(1, 5):
            driver.get(f'https://gu.cards/?marketplace=with_listings&page={page}&quality_diamond=on')
            driver.find_elements_by_css_selector('div.js-card-with-trading-buttons')
            response_pages = response.replace(body=driver.page_source)

            for res in response_pages.css(all_cards):
                item['name'] = res.css(name_base).xpath('string()').get()
                item['price'] = res.css(price_base).xpath('string()').get()
                item['currency'] = ETH
                item['quality'] = Diamond
                item['purchase_URL'] = base_url + res.css(purchase_URL_base).get()
                card_id = re.sub('\\D', '', res.css(purchase_URL_base).get())
                item['image_URL'] = image_URL_base(card_id, 1)

                yield item

            try:
                driver.implicitly_wait(3)
                driver.find_element_by_css_selector('i.fa-caret-right')
            except Exception:
                return

        driver.quit()



def handler():
    process = CrawlerProcess()

    process.crawl(guCardsShadow_Spider)
    process.crawl(guCardsGold_Spider)
    process.crawl(guCardsDiamond_Spider)

    process.start()

