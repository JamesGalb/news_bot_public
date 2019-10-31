# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class CIAGovSpider(scrapy.Spider):
    name = 'cia_gov'
    start_urls = ['https://www.cia.gov/news-information/speeches-testimony',
                  'https://www.cia.gov/news-information/press-releases-statements']

    def parse(self, response):
        items = []
        for element in response.css('ul.topic_list li')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('span.topicDescription::text').extract_first()
            item['link'] = "https://www.cia.gov" + element.css('span.summary a::attr(href)').extract_first()
            items.append(item)
        return items
