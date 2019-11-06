# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class GOPResearchSpider(scrapy.Spider):
    name = 'gop_research'
    start_urls = ['https://www.gop.com/research/']

    def parse(self, response):
        items = []
        for element in response.css('a.ng-binding')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.gop.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
