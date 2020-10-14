# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium.webdriver import Chrome, ChromeOptions
from scrapy.http import HtmlResponse
import time
import random

from selenium.webdriver.common.keys import Keys


class godsOfficial_Selenium_Middleware(object):

    def process_request(self, request, spider):
        options = ChromeOptions()
        # options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(60)

        driver.get('https://godsunchained.com/')
        driver.get('https://godsunchained.com/account/login')
        time.sleep(5)

        def singin():
            time.sleep(random.randrange(2, 4))
            email = driver.find_elements_by_css_selector("input.ng-untouched")[0]
            email.send_keys("testgastodingtalkbot@gmail.com")
            time.sleep(random.randrange(2, 4))
            keypass = driver.find_elements_by_css_selector("input.ng-untouched")[1]
            keypass.send_keys("kebabman")
            driver.find_element_by_css_selector("cerberus-checkbox").click()
            time.sleep(random.randrange(2, 4))
            Gologin = driver.find_element_by_css_selector("gu-primary-hex-button")
            Gologin.click()

        singin()
        # time.sleep(random.randrange(2, 4))
        # try:
        #     driver.find_element_by_css_selector("div.captchaContainer").click()
        #     driver.get(
        #         'https://godsunchained.com/marketplace/search?groupby=name&sortby=timestamp&orderby=desc&currentpage=1&perpage=300&assettype=card')
        #     driver.get('https://godsunchained.com/account/login')
        #     singin()
        #     time.sleep(random.randrange(2, 4))
        # except Exception as e:
        #     print(e)
        #     pass

        # サイト内で他の画面に遷移させたければ
        time.sleep(20)
        driver.get('https://godsunchained.com/marketplace/search?groupby=name&sortby=timestamp&orderby=desc&currentpage=1&perpage=1800')
        driver.find_elements_by_css_selector('div.assets__cardItem')


        driver.execute_script('scroll(0, document.body.scrollHeight)')
        time.sleep(0.5)

        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )

        driver.quit()


class GodsofficialSpiderMiddleware(object):
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


class GodsofficialDownloaderMiddleware(object):
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
