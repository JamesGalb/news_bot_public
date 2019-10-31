# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class CommerceGovSpider(scrapy.Spider):
    name = 'commerce_gov'
    start_urls = ['https://www.commerce.gov/news/press-releases',
                  'https://www.commerce.gov/news/speeches',
                  'https://www.commerce.gov/news/fact-sheets',
                  'https://www.commerce.gov/news/op-eds']

    def parse(self, response):
        items = []
        for element in response.css('article.node--type-news h2 a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('span::text').extract_first()
            item['link'] = "https://www.commerce.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
