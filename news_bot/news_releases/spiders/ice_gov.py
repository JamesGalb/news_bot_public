# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class ICEGovSpider(XMLFeedSpider):
    name = 'ice_gov'
    start_urls = ['https://www.ice.gov/rss/news/375',
                  'https://www.ice.gov/rss/ice-breaking-news',
                  'https://www.ice.gov/rss/speeches-testimony']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['source_id'] = 'ICE'
        item['summary'] = None
        item['content'] = None
        return item
