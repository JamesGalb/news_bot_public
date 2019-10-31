# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class GOPSpider(scrapy.Spider):
    name = 'gop_spider'
    start_urls = ['https://www.gop.com/press-releases']

    def parse(self, response):
        items = []
        for element in response.css('div.news-entry-text h2.entry-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.gop.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
