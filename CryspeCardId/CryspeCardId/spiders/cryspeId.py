# -*- coding: utf-8 -*-
import scrapy
import re
import requests
import json
from ..items import CryspecardidItem


class CryspeidSpider(scrapy.Spider):
    name = 'cryspeId'
    allowed_domains = ['cryptospells.jp/cards']
    start_urls = ['http://cryptospells.jp/cards/']
    # allowed_domains = ['cryptospells.jp/cryptospells']
    # start_urls = ['http://cryptospells.jp/cryptospells/']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'CryspeCardId.middlewares.Cryspecardid_selenium_Middleware': 540,
        },
        'BOT_NAME': 'CryspeCardId',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'CryspeCardId.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['CryspeCardId.spiders'],
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'cryspe_spl_Id.csv',
    }

    def parse(self, response):
        cardID = CryspecardidItem()
        card_number = []
        for res in response.css('span.card__info--card-number'):
            cardid = res.xpath('string()').get()
            card_number.append(re.sub(r'# ', '', cardid))

        for card in card_number:
            result = requests.get(f'https://cryptospells.jp/public_api/cards/{card}.json').json()
            cardID['id'] = result['card_number']
            cardID['name_ja'] = result['name']['ja']
            name_en = result['name']['en']
            name_en2 = re.sub(r',', '', name_en)
            cardID['name_en'] = re.sub(r"'", "\\'", name_en2)
            cardID['cost'] = result['cost']
            cardID['AP'] = result['power']
            cardID['HP'] = result['life']
            cardID['effect'] = result['ability']['ja']
            cardID['image_url'] = result['image_url']['ja']
            effect_en = result['ability']['en']
            effect_en2 = re.sub(r',', '', effect_en)
            cardID['effect_en'] = re.sub(r"'", "\\'", effect_en2)
            cardID['image_url_en'] = result['image_url']['en']

            if result['card_type'] == 'unit':
                cardID['card_type_id'] = 1
            if result['card_type'] == 'spell':
                cardID['card_type_id'] = 2
            if result['card_type'] == 'magic_bottle':
                cardID['card_type_id'] = 3

            if result['color'] == 'neutral':
                cardID['color_id'] = 1
            if result['color'] == 'red':
                cardID['color_id'] = 2
            if result['color'] == 'blue':
                cardID['color_id'] = 3
            if result['color'] == 'green':
                cardID['color_id'] = 4
            if result['color'] == 'white':
                cardID['color_id'] = 5
            if result['color'] == 'black':
                cardID['color_id'] = 6

            if result['rarity'] == 'bronze':
                cardID['rarelity_id'] = 1
            if result['rarity'] == 'silver':
                cardID['rarelity_id'] = 2
            if result['rarity'] == 'gold':
                cardID['rarelity_id'] = 3
            if result['rarity'] == 'legend':
                cardID['rarelity_id'] = 4
            if result['rarity'] == 'limited_legend':
                cardID['rarelity_id'] = 5

            if result['kind'] == 'angel':
                cardID['tribe_id'] = 1
            if result['kind'] == 'soldier':
                cardID['tribe_id'] = 2
            if result['kind'] == 'beast':
                cardID['tribe_id'] = 3
            if result['kind'] == 'demon':
                cardID['tribe_id'] = 4
            if result['kind'] == 'witch':
                cardID['tribe_id'] = 5
            if result['kind'] == 'dragon':
                cardID['tribe_id'] = 6
            if result['kind'] == 'fairy':
                cardID['tribe_id'] = 7
            if result['kind'] == 'land':
                cardID['tribe_id'] = 8
            if result['kind'] == 'spl':
                cardID['tribe_id'] = 9

            yield cardID


