# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class TransportationGovBlogSpider(scrapy.Spider):
    name = 'transportation_gov_blog'
    start_urls = ['https://www.transportation.gov/blog/connections']

    def parse(self, response):
        items = []
        for element in response.css('div.blog-header h1.title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.transportation.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
