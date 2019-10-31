# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class HHSGovNewsSpider(scrapy.Spider):
    name = 'hhs_gov_news'
    start_urls = ['https://www.hhs.gov/about/news/index.html']

    def parse(self, response):
        items = []
        for element in response.css('div.news-listing-row div.views-field-title span a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.hhs.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
