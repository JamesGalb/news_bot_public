# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease


class WhitehouseNewsSpider(scrapy.Spider):
    name = 'whitehouse_news'
    start_urls = ['https://www.whitehouse.gov/news/']


    def parse(self, response):
        items = []
        for element in response.css('div.page-results__wrap article'):
            item = NewsRelease()
            item['link'] = element.css('div h2 a::attr(href)').extract_first()
            item['title'] = element.css('div h2 a::text').extract_first()
            items.append(item)
        return items

    #def whitehouse_news_title(self, response):
    #    item = response.meta['item']
    #    item['title'] = response.css('title::text').extract_first()
    #    return item
