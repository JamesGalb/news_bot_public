# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class StateGovSpider(scrapy.Spider):
    name = 'state_gov'
    start_urls = ['https://www.state.gov/press-releases/',
                  'https://www.state.gov/speeches-secretary-pompeo/',
                  'https://www.state.gov/department-press-briefings/']

    def parse(self, response):
        items = []
        for element in response.css('li.collection-result a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = 'STATE'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
