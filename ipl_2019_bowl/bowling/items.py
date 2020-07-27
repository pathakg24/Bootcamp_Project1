# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BowlingItem(scrapy.Item):
    player = scrapy.Field()
    mat = scrapy.Field()
    inns = scrapy.Field()
    overs = scrapy.Field()
    mdns = scrapy.Field()
    runs = scrapy.Field()
    wkts = scrapy.Field()
    bbi = scrapy.Field()
    bowl_ave = scrapy.Field()
    econ = scrapy.Field()
    bowl_sr = scrapy.Field()
    fours = scrapy.Field()
    fives = scrapy.Field()
    ct = scrapy.Field()
    st = scrapy.Field()
