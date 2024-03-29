# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    table = "csdn_detail"
    title = scrapy.Field()
    number = scrapy.Field()
    price = scrapy.Field()
    cover = scrapy.Field()
    teacher = scrapy.Field()
    intro = scrapy.Field()
    sections = scrapy.Field()
    # pass
