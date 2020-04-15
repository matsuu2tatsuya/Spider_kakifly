# -*- coding: utf-8 -*-
import scrapy


class TokenTroveSpiderSpider(scrapy.Spider):
    name = 'token_trove_spider'
    allowed_domains = ['tokentrove.com']
    start_urls = ['https://tokentrove.com/GodsUnchainedCards?perPage=120']

    def parse(self, response):
        pass
