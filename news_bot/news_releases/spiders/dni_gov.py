# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class DNIGovSpider(scrapy.Spider):
    name = 'dni_gov'
    start_urls = ['https://www.dni.gov/index.php/newsroom']

    def parse(self, response):
        items = []
        for element in response.css('h3.catItemTitle a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.dni.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'DNI'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
