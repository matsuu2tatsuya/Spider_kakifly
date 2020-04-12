# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium.webdriver import Chrome, ChromeOptions
from scrapy.http import HtmlResponse
import time

"""
gu_cardsのselenium処理を書いて行く。qualityで分ける。
かなり大量になるが、変えるのはdriver.get('url')のみ
"""

# Shadow
class guCardsShadow_1_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=1&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsShadow_2_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=2&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsShadow_3_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=3&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsShadow_4_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=4&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsShadow_5_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=5&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsShadow_6_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=6&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()


class guCardsShadow_7_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=7&quality_shadow=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()


# Gold
class guCardsGold_1_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=1&quality_gold=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsGold_2_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=2&quality_gold=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsGold_3_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=3&quality_gold=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()


# Diamond
class guCardsDiamond_1_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=1&quality_diamond=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsDiamond_2_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=2&quality_diamond=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()

class guCardsDiamond_3_Middleware(object):
    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get('https://gu.cards/?marketplace=with_listings&page=3&quality_diamond=on')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        driver.quit()


class GuCardsSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GuCardsDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
