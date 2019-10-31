# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class DOLGovBlogSpider(scrapy.Spider):
    name = 'dol_gov_blog'
    start_urls = ['https://blog.dol.gov/']

    def parse(self, response):
        items = []
        for element in response.css('h2.post-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://blog.dol.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
