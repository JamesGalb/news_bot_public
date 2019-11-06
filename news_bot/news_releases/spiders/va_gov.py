# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class VAGovSpider(scrapy.Spider):
    name = 'va_gov'
    start_urls = ['https://www.va.gov/opa/pressrel/']

    def parse(self, response):
        items = []
        for element in response.css('p.speech-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.va.gov/opa/pressrel/" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'VA'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
