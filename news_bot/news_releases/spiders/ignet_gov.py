# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class IGNetGovSpider(scrapy.Spider):
    name = 'ignet_gov'
    custom_settings = {'EXPECTED': 6}
    start_urls = ['https://www.ignet.gov/content/newsroom',
                  'https://www.ignet.gov/content/events']    

    def parse(self, response):
        items = []
        for element in response.css('div.field-item ul li a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.ignet.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'OIG'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
