# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CryspecardidItem(scrapy.Item):
    id = scrapy.Field()
    name_ja = scrapy.Field()
    name_en = scrapy.Field()
    cost = scrapy.Field()
    AP = scrapy.Field()
    HP = scrapy.Field()
    effect = scrapy.Field()
    image_url = scrapy.Field()
    effect_en = scrapy.Field()
    image_url_en = scrapy.Field()
    card_type_id = scrapy.Field()
    color_id = scrapy.Field()
    rarelity_id = scrapy.Field()
    tribe_id = scrapy.Field()

