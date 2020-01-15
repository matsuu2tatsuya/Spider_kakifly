# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

"""
MYSQLのItemテーブルに入れるもの
-> ID, name, price_ETH, price_SPL, price_JPY, buy_transaction_URL
-> sell_transaction_URL_ETH, buy_transaction_URL_JPY, image_URL
の９個。
"""

import scrapy


class EthmarketItem(scrapy.Item):
    """
    名前、値段（ETH）、購入URL、画像URLのそれぞれの箱を用意。他はNULL
    """
    ids = scrapy.Field()
    ID = scrapy.Field()
    name = scrapy.Field()
    price_ETH = scrapy.Field()
    price_SPL = scrapy.Field()
    price_JPY = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    sell_transaction_URL_ETH = scrapy.Field()
    buy_transaction_URL_JPY = scrapy.Field()
    image_URL = scrapy.Field()


class MagiItem(scrapy.Item):
    """
    （magi） 名前、値段、購入URL、画像URLの箱。他はNULL
    """
    ids = scrapy.Field()
    ID = scrapy.Field()
    name = scrapy.Field()
    price_ETH = scrapy.Field()
    price_SPL = scrapy.Field()
    price_JPY = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    sell_transaction_URL_ETH = scrapy.Field()
    buy_transaction_URL_JPY = scrapy.Field()
    image_URL = scrapy.Field()


class Cryptospells_Item(scrapy.Item):
    """
    (クリプトスペルズ内マーケット)　名前、ID、値段（SPL）、販売期限、購入URL、画像URLの箱。他はNULL
    """
    ids = scrapy.Field()
    ID = scrapy.Field()
    name = scrapy.Field()
    price_ETH = scrapy.Field()
    price_SPL = scrapy.Field()
    price_JPY = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    sell_transaction_URL_ETH = scrapy.Field()
    buy_transaction_URL_JPY = scrapy.Field()
    image_URL = scrapy.Field()


class spider_DEX_Item(scrapy.Item):
    """
    spider_DEX　の名前（en）、ID、画像URL、購入URL。他はNULL
    """
    ids = scrapy.Field()
    ID = scrapy.Field()
    name = scrapy.Field()
    price_ETH = scrapy.Field()
    price_SPL = scrapy.Field()
    price_JPY = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    sell_transaction_URL_ETH = scrapy.Field()
    buy_transaction_URL_JPY = scrapy.Field()
    image_URL = scrapy.Field()
