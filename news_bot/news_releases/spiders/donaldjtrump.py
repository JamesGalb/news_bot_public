# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class DonaldjtrumpSpider(scrapy.Spider):
    name = 'donaldjtrump'
    start_urls = ['https://www.donaldjtrump.com/media/']

    def parse(self, response):
        items = []
        for element in response.css('a.news-item')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('h5::text').extract_first()
            item['link'] = "https://www.donaldjtrump.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        for element in response.css('a.video')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('div h5::text').extract_first()
            item['link'] = "https://www.donaldjtrump.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
