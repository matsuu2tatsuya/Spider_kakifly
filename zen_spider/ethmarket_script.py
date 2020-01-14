from zen_spider.spiders import zen_spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

from scrapy.settings import Settings

from zen_spider import settings as my_settings

crawler_settings = Settings()
crawler_settings.setmodule(my_settings)
process = CrawlerProcess(settings=crawler_settings)


class Scraper:
    def __init__(self):
        settings_file_path = 'zen_spider.zen_spider.settings'  # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = zen_spider  # The spider you want to crawl

    def run_spiders(self):
        self.process.crawl(self.spider)
        self.process.start()