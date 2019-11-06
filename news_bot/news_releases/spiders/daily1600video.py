# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import time

class Daily1600videoSpider(scrapy.Spider):
    name = 'daily1600video'
    start_urls = ['https://www.whitehouse.gov/1600daily/']

    def parse(self, response):
        items = []
        for element in response.css('div.video__embed iframe'):
            item = NewsRelease()
            item['link'] = element.css('::attr(src)').extract_first()
            item['source_id'] = '1600'
            item['summary'] = None
            item['content'] = None
            request = scrapy.Request(item['link'], callback=self.parse_daily1600video_get_video)
            request.meta['item'] = item
            items.append(request)
        return items
    
    def parse_daily1600video_get_video(self, response):
        item = response.meta['item']
        item['link'] = response.css('div.ytp-title-text a::attr(href)').extract_first()
        item['title'] = response.css('div.ytp-title-text a::text').extract_first()
        return item
