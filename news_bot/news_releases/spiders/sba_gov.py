# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class SBAGovSpider(scrapy.Spider):
    name = 'sba_gov'
    start_urls = ['https://www.sba.gov/about-sba/sba-newsroom/press-releases-media-advisories',
                  'https://www.sba.gov/about-sba/sba-newsroom/congressional-testimony']
    def parse(self, response):
        items = []
        for element in response.css('div.view-about-newsroom div table tbody tr td.views-field-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.sba.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'SBA'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
