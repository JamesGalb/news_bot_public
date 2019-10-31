# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import time

class Daily1600picSpider(scrapy.Spider):
    name = 'daily1600pic'
    start_urls = ['https://www.whitehouse.gov/1600daily/']

    def parse(self, response):
        items = []
        for element in response.css('figure.image')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('figcaption.image__caption::text').extract_first()
            item['link'] = element.css('div.image__download a::attr(href)').extract_first()
            items.append(item)
        return items
