# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class OIGGovSpider(scrapy.Spider):
    name = 'oig_gov'
    custom_settings = {'EXPECTED': 3}
    start_urls = ['https://oig.justice.gov/press/']    

    def parse(self, response):
        items = []
        for element in response.css('div.tab-content p a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://oig.justice.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
