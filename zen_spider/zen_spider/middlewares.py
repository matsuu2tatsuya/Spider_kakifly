# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium.webdriver import Chrome, ChromeOptions, Remote
from scrapy.http import HtmlResponse

import time


class SeleniumMiddleware(object):
    """
    spider_DEXのselenium
    """

    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)

        driver.get('https://www.spiderdex.com/assets/5d35228f74ba04002ac53d9c')
        time.sleep(0.5)
        input_element = driver.find_elements_by_css_selector('div.filterattributevalue > div.item')[5]
        input_element.click()
        time.sleep(0.5)

        for div in driver.find_elements_by_xpath('//div[@class="assetscontentitem"]'):
            time.sleep(0.5)
            div.find_element_by_css_selector('div.assetimghover').click()
            handle_array = driver.window_handles
            driver.switch_to.window(handle_array[1])
            time.sleep(0.5)

        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )

        time.sleep(0.5)
        driver.quit()



class cryspe_SeleniumMiddleware(object):
    """
    crypto_spellsのselenium
    """

    def process_request(self, request, spider):
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(options=options)

        driver.get('https://cryptospells.jp/trades')
        time.sleep(0.5)
        input_element = driver.find_element_by_xpath("//span[@class='checkmark']")
        input_element.click()
        time.sleep(0.5)

        for _ in range(20):
            driver.execute_script('scroll(0, document.body.scrollHeight)')
            time.sleep(2.0)

        return HtmlResponse(
            driver.current_url,
            body=driver.page_source,
            encoding='utf-8',
            request=request,
        )

        driver.quit()


