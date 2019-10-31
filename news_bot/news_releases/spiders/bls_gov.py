# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class BLSGovSpider(XMLFeedSpider):
    name = 'bls_gov'
    start_urls = ['https://www.bls.gov/feed/leave.rss',
                  'https://www.bls.gov/feed/atus.rss']
    iterator = 'html'
    itertag = 'entry'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/@href').get()
        item['source_id'] = 'BLS'
        item['summary'] = None
        item['content'] = None
        return item
