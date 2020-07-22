# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GodsMiimeItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    quality = scrapy.Field()
    purchase_URL = scrapy.Field()
    image_URL = scrapy.Field()
