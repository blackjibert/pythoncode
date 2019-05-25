# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class ScrapysplashjdItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     title =scrapy.Field()
#     # pass

class MongoPipelineItem(scrapy.Item):
    collection = 'products'
    title = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    deal = scrapy.Field()