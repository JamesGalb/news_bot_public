# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class BLSGovTEDSpider(scrapy.Spider):
    name = 'bls_gov_ted'
    start_urls = ['https://stats.bls.gov/opub/ted/year.htm']

    def parse(self, response):
        items = []
        for element in response.css('h6 ~ ul li a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://stats.bls.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'BLS'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
