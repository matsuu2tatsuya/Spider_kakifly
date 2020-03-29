# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium.webdriver import Chrome, ChromeOptions, Remote
from scrapy.http import HtmlResponse
import time


class DEX_SeleniumMiddleware(object):

    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(10)

        driver.get('https://www.spiderdex.com/assets/5d35228f74ba04002ac53d9c')
        input_element = driver.find_elements_by_css_selector('div.filterattributevalue > div.item')[5]
        input_element.click()

        for div in driver.find_elements_by_xpath('//div[@class="assetscontentitem"]'):
            div.find_element_by_css_selector('div.assetimghover').click()
            handle_array = driver.window_handles
            driver.switch_to.window(handle_array[1])

        f = HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        if f:
            return f
            driver.quit()


class cryspe_SeleniumMiddleware(object):

    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(30)

        driver.get('https://cryptospells.jp/trades')
        input_element = driver.find_element_by_xpath("//span[@class='checkmark']")
        input_element.click()
        h = 0
        r = []

        while h < 200:
            driver.execute_script('scroll(0, document.body.scrollHeight)')
            time.sleep(0.3)
            r.append(len(driver.find_elements_by_css_selector('div.col-card')))
            time.sleep(0.3)
            print(r)
            h = h + 1
            print(h)
            if h == 200:
                # print('BREEK')
                break
            if len(r) > 2:
                if r[-1] - r[-2] != 0 and r[-1] - r[-2] < 20:
                    break
            if len(r) > 7:
                if r[-1] == r[-7]:
                    break

        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )

        driver.quit()


class ZenSpiderSpiderMiddleware(object):
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


class ZenSpiderDownloaderMiddleware(object):
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
