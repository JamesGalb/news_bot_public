# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class TransportationGovSpider(scrapy.Spider):
    name = 'transportation_gov'
    start_urls = ['https://www.transportation.gov/press-releases']

    def parse(self, response):
        items = []
        for element in response.css('div.view-display-id-page_press_releases div table tbody tr td.views-field-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.transportation.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'DOT'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
