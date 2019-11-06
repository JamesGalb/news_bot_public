# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class USUNGovSpider(scrapy.Spider):
    name = 'usun_gov'
    start_urls = ['https://usun.usmission.gov/category/remarks-and-highlights/']

    def parse(self, response):
        items = []
        for element in response.css('header h2.entry-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = 'USUN'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
