# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

"""
MYSQLのItemテーブルに入れるもの
{ID(auto),name(id or card_name),price(int),currency(ETH),purchase_URL,image_URL}の６つ。
"""

import scrapy


class EthmarketItem(scrapy.Item):
    """
    イーサマーケット：ETH
    """
    ID = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    image_URL = scrapy.Field()


class EthmarketItem_JPY(scrapy.Item):
    """
    イーサマーケット：JPY
    """
    ID = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    image_URL = scrapy.Field()


class MagiItem(scrapy.Item):
    """
    magi:ETH
    """
    ID = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    image_URL = scrapy.Field()


class Cryptospells_Item(scrapy.Item):
    """
    クリプトスペルズ内マーケット:SPL
    """
    ID = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    image_URL = scrapy.Field()


class Spider_DEX_Item(scrapy.Item):
    """
    spider_DEX :ETH
    """
    ID = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    buy_transaction_URL = scrapy.Field()
    image_URL = scrapy.Field()
