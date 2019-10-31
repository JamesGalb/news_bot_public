# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class TreasuryGovSpider(scrapy.Spider):
    name = 'treasury_gov'
    start_urls = ['https://home.treasury.gov/news/press-releases']

    def parse(self, response):
        items = []
        for element in response.css('div.content--2col__body div h3 a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://home.treasury.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
