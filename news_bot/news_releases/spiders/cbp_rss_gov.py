# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class CBPrssGovSpider(XMLFeedSpider):
    name = 'cbp_rss_gov'
    start_urls = ['https://www.cbp.gov/rss/newsroom/media-releases',
                  'https://www.cbp.gov/rss/newsroom',
                  'https://www.cbp.gov/rss/border-construction',
                  'https://www.cbp.gov/rss/border-security']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['source_id'] = 'CBP'
        item['summary'] = None
        item['content'] = None
        return item
