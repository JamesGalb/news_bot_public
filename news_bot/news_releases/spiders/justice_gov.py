# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class JusticeGovSpider(scrapy.Spider):
    name = 'justice_gov'
    custom_settings = {'EXPECTED': 6}
    start_urls = ['https://www.justice.gov/news',
                  'https://www.justice.gov/videos']    

    def parse(self, response):
        items = []
        for element in response.css('div.views-field-title span a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.justice.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
