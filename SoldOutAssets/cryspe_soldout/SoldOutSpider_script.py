from cryspe_soldout.spiders import cryspe_soldout_spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


class Scraper:
    def __init__(self):
        settings = cryspe_soldout_spider.settings
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = cryspe_soldout_spider  # The spider you want to crawl

    def run_spiders(self):
        self.process.crawl(self.spider)
        self.process.start()
        print('Spider SUCCESS !!!')
