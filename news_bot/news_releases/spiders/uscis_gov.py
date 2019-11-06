# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class USCISGovSpider(XMLFeedSpider):
    name = 'uscis_gov'
    start_urls = ['https://www.uscis.gov/rss-news/1/1125?title=News%20Releases&topic_id=1',
                  'https://www.dhs.gov/testimony/(USCIS)-U.S.-Citizenship-and-Immigration-Services/rss.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['source_id'] = 'USCIS'
        item['summary'] = None
        item['content'] = None
        return item
