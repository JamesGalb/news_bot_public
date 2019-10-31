# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class TreasuryStoriesGovSpider(scrapy.Spider):
    name = 'treasury_stories_gov'
    start_urls = ['https://home.treasury.gov/news/featured-stories']

    def parse(self, response):
        items = []
        for element in response.css('div.featured-stories--vertical__headline a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://home.treasury.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
