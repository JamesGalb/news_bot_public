# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class SpaceCommGovSpider(scrapy.Spider):
    name = 'space_comm_gov'
    start_urls = ['https://www.spacecom.mil/MEDIA/NEWS-ARTICLES/']

    def parse(self, response):
        items = []
        for element in response.css('div.item p.title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = 'SPACE'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
