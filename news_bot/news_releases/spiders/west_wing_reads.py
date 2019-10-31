# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import time

class WestWingReadsSpider(scrapy.Spider):
    name = 'west_wing_reads'
    start_urls = ['https://www.whitehouse.gov/westwingreads/']

    def parse(self, response):
        items = []
        for element in response.css('div.page-content__content p a'):
            item = NewsRelease()
            item['link'] = element.css('::attr(href)').extract_first()
            request = scrapy.Request(item['link'], callback=self.parse_west_wing_read_title)
            request.meta['item'] = item
            items.append(request)
        return items
    
    def parse_west_wing_read_title(self, response):
        item = response.meta['item']
        item['title'] = response.css('title::text').extract_first()
        return item
