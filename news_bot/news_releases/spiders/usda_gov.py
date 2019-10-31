# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class USDAGovSpider(scrapy.Spider):
    name = 'usda_gov'
    start_urls = ['https://www.usda.gov/media/blog']

    def parse(self, response):
        items = []
        for element in response.css('div.usda-blog-teaser-content h3 a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('span::text').extract_first()
            item['link'] = "https://www.usda.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items