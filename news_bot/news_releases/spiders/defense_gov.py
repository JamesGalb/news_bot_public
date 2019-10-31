# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import pdb

class DefenseGovSpider(scrapy.Spider):
    name = 'defense_gov'
    custom_settings = {'EXPECTED': 9}
    start_urls = ['https://www.defense.gov/Newsroom/Publications/',
                  'https://www.defense.gov/Newsroom/Speeches/',
                  'https://www.defense.gov/Newsroom/releases/']

    def parse(self, response):
        items = []
        for element in response.css('div.lside a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            items.append(item)
        return items
