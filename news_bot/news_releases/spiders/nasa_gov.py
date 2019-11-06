# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class NASAGovSpider(XMLFeedSpider):
    name = 'nasa_gov'
    start_urls = ['https://www.nasa.gov/rss/dyn/breaking_news.rss',
                  'https://www.nasa.gov/rss/dyn/shuttle_station.rss',
                  'https://www.nasa.gov/rss/dyn/solar_system.rss',
                  'https://www.nasa.gov/rss/dyn/earth.rss',
                  'https://www.nasa.gov/rss/dyn/aeronautics.rss']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['source_id'] = 'NASA'
        item['summary'] = None
        item['content'] = None
        return item
