# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class EducationGovSpider(scrapy.Spider):
    name = 'education_gov'
    start_urls = ['https://www.ed.gov/news/press-releases']

    def parse(self, response):
        items = []
        for element in response.css('div.item-list ul li div.views-field-field-custom-title h2 a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.ed.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
