# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import pdb
class FBIGovSpider(scrapy.Spider):
    name = 'fbi_gov'
    custom_settings = {'EXPECTED': 6}
    start_urls = ['https://www.fbi.gov/news/speeches',
                  'https://www.fbi.gov/news/testimony']

    def parse(self, response):
        items = []
        for element in response.css('div.col-lg-10 p.title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            items.append(item)
        return items
