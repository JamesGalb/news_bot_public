# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class OversightGovSpider(scrapy.Spider):
    name = 'oversight_gov'
    start_urls = ['https://oversight.gov/reports']    

    def parse(self, response):
        items = []
        for element in response.css('td.views-field-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://oversight.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'OIG'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
