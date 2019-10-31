# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class SECGovSpider(scrapy.Spider):
    name = 'sec_gov'
    start_urls = ['https://www.sec.gov/news/pressreleases',
                  'https://www.sec.gov/news/statements',
                  'https://www.sec.gov/news/speeches',
                  'https://www.sec.gov/news/testimony']
    def parse(self, response):
        items = []
        for element in response.css('tr td.views-field-field-display-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.sec.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
