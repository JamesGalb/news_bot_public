# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class JointChiefsSpider(scrapy.Spider):
    name = 'joint_chiefs_gov'
    start_urls = ['https://www.jcs.mil/Media/News/']

    def parse(self, response):
        items = []
        for element in response.css('div.item span.title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            items.append(item)
        return items
