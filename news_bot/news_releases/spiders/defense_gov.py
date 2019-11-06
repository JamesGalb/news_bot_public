# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease
import pdb

class DefenseGovSpider(scrapy.Spider):
    name = 'defense_gov'
    start_urls = ['https://www.defense.gov/Newsroom/Publications/',
                  'https://www.defense.gov/Newsroom/Speeches/',
                  'https://www.defense.gov/Newsroom/releases/',
                  'https://www.defense.gov/Newsroom/Transcripts/']

    def parse(self, response):
        items = []
        for element in response.css('div.lside a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = 'DOD'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
