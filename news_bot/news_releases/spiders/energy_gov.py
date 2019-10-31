# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class EnergyGovSpider(scrapy.Spider):
    name = 'energy_gov'
    start_urls = ['https://www.energy.gov/listings/energy-news',
                  'https://www.energy.gov/listings/energy-remarks',
                  'https://www.energy.gov/listings/media-advisories']

    def parse(self, response):
        items = []
        for element in response.css('div.node-article div.content a.title-link')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.energy.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
