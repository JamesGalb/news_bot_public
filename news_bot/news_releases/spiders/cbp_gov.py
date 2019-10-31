# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class CBPGovSpider(scrapy.Spider):
    name = 'cbp_gov'
    start_urls = ['https://www.cbp.gov/newsroom/media-releases/all?title=&field_newsroom_type_tid_1=81',
                  'https://www.cbp.gov/newsroom/media-releases/all?title=&field_newsroom_type_tid_1=54',
                  'https://www.cbp.gov/newsroom/speeches',
                  'https://www.cbp.gov/newsroom/news/news-from-cbp']

    def parse(self, response):
        items = []
        for element in response.css('div.views-field-title span.field-content a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.cbp.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
