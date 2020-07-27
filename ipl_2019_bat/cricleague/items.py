# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CricleagueItem(scrapy.Item):
    player = scrapy.Field()
    mat = scrapy.Field()
    inns = scrapy.Field()
    no = scrapy.Field()
    runs = scrapy.Field()
    hs = scrapy.Field()
    ave = scrapy.Field()
    bf = scrapy.Field()
    sr = scrapy.Field()
    hundreds = scrapy.Field()
    fiftys = scrapy.Field()
    zeros = scrapy.Field()
    fours = scrapy.Field()
    sixs = scrapy.Field()