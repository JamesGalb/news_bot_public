# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#Add Items
class NewsRelease(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    source_id = scrapy.Field()
    summary = scrapy.Field()
    content = scrapy.Field()
