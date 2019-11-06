# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class EPAGovSpider(scrapy.Spider):
    name = 'epa_gov'
    start_urls = ['https://www.epa.gov/newsreleases/search/field_press_office/headquarters']

    def parse(self, response):
        items = []
        for element in response.css('div.node-news-release h3.teaser-title a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.epa.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'EPA'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
