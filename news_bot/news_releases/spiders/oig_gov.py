# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class OIGGovSpider(scrapy.Spider):
    name = 'oig_gov'
    start_urls = ['https://oig.justice.gov/press/']    

    def parse(self, response):
        items = []
        for element in response.css('div.tab-content p a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://oig.justice.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'OIG'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
