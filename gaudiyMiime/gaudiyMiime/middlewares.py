# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium.webdriver import Chrome, ChromeOptions
from scrapy.http import HtmlResponse
import time


class gaudiySelenium_Middleware(object):

    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(20)

        driver.get('https://gaudiy.com/community_details/avJEInz3EXlxNXKMSWxR')
        time.sleep(0.3)
        input_element = driver.find_elements_by_css_selector('span:nth-child(5) > button > span > p')[0]
        if input_element:
            input_element.click()
        time.sleep(0.3)
        nft_element = driver.find_elements_by_css_selector('span.MuiTab-wrapper')[0]
        if nft_element:
            nft_element.click()
        source_element = driver.find_element_by_css_selector('label.MuiFormControlLabel-root')
        if source_element:
            # source_element.click()
            time.sleep(1.0)
            link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[-2]
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            time.sleep(0.3)
            while link != driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[-2]:
                link = driver.find_elements_by_css_selector('button > div > p:nth-child(1)')[-2]
                driver.execute_script("arguments[0].scrollIntoView(true);", link)
                time.sleep(0.3)

        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )
        time.sleep(0.5)
        driver.quit()



class miimeSelenium_Middleware(object):

    def process_request(self, request, spider):
        options = ChromeOptions()
        # options.headless = True
        driver = Chrome(options=options)
        driver.implicitly_wait(20)

        driver.get('https://miime.io/assets/2')
        input_element = driver.find_elements_by_css_selector(
            '#__layout > div > main > div.filterButtonBar > div > div:nth-child(5) > a')[0]
        input_element.click()
        all_item = driver.find_elements_by_css_selector('#__layout > div > main > div.filterButtonBar > div > div.filterButtonBar__filterButton.filterButtonBar__filterButton--saleFilter > div > div:nth-child(2)')[0]
        all_item.click()
        time.sleep(0.5)
        driver.execute_script('scroll(0, document.body.scrollHeight)')
        more_element = driver.find_element_by_css_selector('#__layout > div > main > div.assetCardList > div.loadMoreButton__Container > div > button.loadMoreButton')
        while more_element:
            try:
                more_element = driver.find_element_by_css_selector('#__layout > div > main > div.assetCardList > '
                                                               'div.loadMoreButton__Container > div > '
                                                               'button.loadMoreButton')
            except Exception:
                break
            time.sleep(0.5)
            if more_element:
                try:
                    more_element.click()
                except Exception:
                    break
            else:
                break

        # print('全て表示されているはず。')
        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )

        time.sleep(0.5)
        driver.quit()



class GaudiymiimeSpiderMiddleware(object):
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


class GaudiymiimeDownloaderMiddleware(object):
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
