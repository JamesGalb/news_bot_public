# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class USAidGovSpider(XMLFeedSpider):
    name = 'usaid_gov'
    start_urls = ['https://www.usaid.gov/rss/press-releases.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['source_id'] = 'USAID'
        item['summary'] = None
        item['content'] = None
        return item
