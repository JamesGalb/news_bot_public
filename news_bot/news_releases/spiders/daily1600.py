# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import time

class Daily1600Spider(scrapy.Spider):
    name = 'daily1600'
    start_urls = ['https://www.whitehouse.gov/1600daily/']

    def parse(self, response):
        items = []
        for element in response.css('div.page-content__content p a'):
            item = NewsRelease()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = '1600'
            item['summary'] = None
            item['content'] = None
            request = scrapy.Request(item['link'], callback=self.parse_daily1600_title)
            request.meta['item'] = item
            items.append(request)
        return items
    
    def parse_daily1600_title(self, response):
        item = response.meta['item']
        item['title'] = response.css('title::text').extract_first()
        return item
