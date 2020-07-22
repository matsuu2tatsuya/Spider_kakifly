# -*- coding: utf-8 -*-
import scrapy
import re
import requests
import json
from ..items import GodscardidItem


class GodscardSpider(scrapy.Spider):
    name = 'GodsCard'
    allowed_domains = ['godsunchained.com']
    start_urls = ['http://godsunchained.com/']

    custom_settings = {
        'BOT_NAME': 'GodsCardId',
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 2,
        'CLOSESPIDER_PAGECOUNT': 10,
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'HTTPCACHE_ENABLED': True,
        # 'HTTPCACHE_EXPIRATION_SECS': 60000,
        'NEWSPIDER_MODULE': 'GodsCardId.spiders',
        # 'ROBOTSTXT_OBEY': True,
        'SPIDER_MODULES': ['GodsCardId.spiders'],
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'GodsCardId.csv',
    }

    def parse(self, response):
        # id, name_en, effect, cost, AP, HP, gods_id, set_id, rarity_id, tribe_id, type_id
        cardID = GodscardidItem()

        response = requests.get(f'https://api.godsunchained.com/v0/proto?page=0').json()
        for result in response['records']:
            cardID['id'] = result['id']
            name_en = result['name']
            name_en2 = re.sub(r',', '', name_en)
            cardID['name_en'] = re.sub(r"'", "\\'", name_en2)

            effect = re.sub(r',', ' ', result['effect'])
            cardID['effect'] = re.sub(r'\u003cbr\u003e', ' ', effect)

            cardID['cost'] = result['mana']
            cardID['AP'] = result['attack']['Int64']
            cardID['HP'] = result['health']['Int64']

            # Gods: 1/neutral, 2/nature, 3/war, 4/death, 5/light, 6/magic, 7/deception
            if result['god'] == 'neutral':
                cardID['gods_id'] = 1
            if result['god'] == 'nature':
                cardID['gods_id'] = 2
            if result['god'] == 'war':
                cardID['gods_id'] = 3
            if result['god'] == 'death':
                cardID['gods_id'] = 4
            if result['god'] == 'light':
                cardID['gods_id'] = 5
            if result['god'] == 'magic':
                cardID['gods_id'] = 6
            if result['god'] == 'deception':
                cardID['gods_id'] = 7

            # SET: 1/genesis, 2/core, 3/etherbots, 4/promo, 5/mythic, 6/trial
            if result['set'] == 'genesis':
                cardID['set_id'] = 1
            if result['set'] == 'core':
                cardID['set_id'] = 2
            if result['set'] == 'etherbots':
                cardID['set_id'] = 3
            if result['set'] == 'promo':
                cardID['set_id'] = 4
            if result['set'] == 'mythic':
                cardID['set_id'] = 5
            if result['set'] == 'trial':
                cardID['set_id'] = 6

            # TRIBE: 1/neutral, 2/aether, 3/amazon, 4/anubian, 5/atlantean, 6/dragon, 7/guild, 8/mystic
            #        9/nether, 10/olympian, 11/structure, 12/viking, 13/wild
            if result['tribe']['String'] == 'neutral':
                cardID['tribe_id'] = 1
            if result['tribe']['String'] == 'aether':
                cardID['tribe_id'] = 2
            if result['tribe']['String'] == 'amazon':
                cardID['tribe_id'] = 3
            if result['tribe']['String'] == 'anubian':
                cardID['tribe_id'] = 4
            if result['tribe']['String'] == 'atlantean':
                cardID['tribe_id'] = 5
            if result['tribe']['String'] == 'dragon':
                cardID['tribe_id'] = 6
            if result['tribe']['String'] == 'guild':
                cardID['tribe_id'] = 7
            if result['tribe']['String'] == 'mystic':
                cardID['tribe_id'] = 8
            if result['tribe']['String'] == 'nether':
                cardID['tribe_id'] = 9
            if result['tribe']['String'] == 'olympian':
                cardID['tribe_id'] = 10
            if result['tribe']['String'] == 'structure':
                cardID['tribe_id'] = 11
            if result['tribe']['String'] == 'viking':
                cardID['tribe_id'] = 12
            if result['tribe']['String'] == 'wild':
                cardID['tribe_id'] = 13

            # TYPE: 1/creature, 2/hero, 3/spell, 4/weapon, 5/god power, 6/advancement
            if result['type'] == 'creature':
                cardID['type_id'] = 1
            if result['type'] == 'hero':
                cardID['type_id'] = 2
            if result['type'] == 'spell':
                cardID['type_id'] = 3
            if result['type'] == 'weapon':
                cardID['type_id'] = 4
            if result['type'] == 'god power':
                cardID['type_id'] = 5
            if result['type'] == 'advancement':
                cardID['type_id'] = 6

            # RARITY: 1/common, 2/rare, 3/epic, 4/legendary, 5/mythic
            if result['rarity'] == 'common':
                cardID['rarity_id'] = 1
            if result['rarity'] == 'rare':
                cardID['rarity_id'] = 2
            if result['rarity'] == 'epic':
                cardID['rarity_id'] = 3
            if result['rarity'] == 'legendary':
                cardID['rarity_id'] = 4
            if result['rarity'] == 'mythic':
                cardID['rarity_id'] = 5


            yield cardID


