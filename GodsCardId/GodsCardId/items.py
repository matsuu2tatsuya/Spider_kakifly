# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GodscardidItem(scrapy.Item):
    id = scrapy.Field()
    image_url = scrapy.Field()
    name_en = scrapy.Field()
    effect = scrapy.Field()
    cost = scrapy.Field()
    AP = scrapy.Field()
    HP = scrapy.Field()
    gods_id = scrapy.Field()
    set_id = scrapy.Field()
    rarity_id = scrapy.Field()
    tribe_id = scrapy.Field()
    type_id = scrapy.Field()


