# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class SpaceAirForceSpider(scrapy.Spider):
    name = 'space_air_force'
    start_urls = ['https://www.afspc.af.mil/News/']

    def parse(self, response):
        items = []
        for element in response.css('section.af2-news-listing ul li div.row div.col-md-9 div.desc h2 a.title')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = 'SPACE'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
