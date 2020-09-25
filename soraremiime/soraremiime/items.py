# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SoraremiimeItem(scrapy.Item):
    player_name = scrapy.Field()
    season = scrapy.Field()
    rarity = scrapy.Field()
    serial_number = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    purchase_URL = scrapy.Field()
    image_URL = scrapy.Field()
    asset_ID = scrapy.Field()
