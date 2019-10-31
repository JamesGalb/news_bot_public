# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class DOLGovSpider(XMLFeedSpider):
    name = 'dol_gov'
    start_urls = ['https://www.dol.gov/rss/releases.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        items = []
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        items.append(item)
        return item
