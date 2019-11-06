# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class USDAGovSpider(scrapy.Spider):
    name = 'usda_gov'
    start_urls = ['https://www.usda.gov/media/press-releases']

    def parse(self, response):
        items = []
        for element in response.css('li.news-releases-item a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.usda.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'USDA'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items