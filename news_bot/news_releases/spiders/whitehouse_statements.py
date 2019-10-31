# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class WhitehouseStatementsSpider(scrapy.Spider):
    name = 'whitehouse_statements'
    custom_settings = {'EXPECTED': 3}
    start_urls = ['https://www.whitehouse.gov/blog']

    def parse(self, response):
        items = []
        for element in response.css('div.views-field-title h3.field-content a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.whitehouse.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
