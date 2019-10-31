# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class DHSGovSpider(scrapy.Spider):
    name = 'dhs_gov'
    start_urls = ['https://www.dhs.gov/news-releases/speeches',
                  'https://www.dhs.gov/news-releases/fact-sheets',
                  'https://www.dhs.gov/news-releases/press-releases']

    def parse(self, response):
        items = []
        for element in response.css('div.view-news-releases-updated div.view-content div.views-row div span a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.dhs.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
