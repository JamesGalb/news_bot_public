# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import pdb

class DefenseGovPressSpider(scrapy.Spider):
    name = 'defense_gov_press'
    start_urls = ['https://www.defense.gov/Newsroom/Press-Products/']

    def parse(self, response):
        items = []
        for element in response.css('div.lside a.title')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            items.append(item)
        return items
