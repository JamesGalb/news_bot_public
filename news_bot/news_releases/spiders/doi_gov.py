# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from news_releases.items import NewsRelease

class DOIGovSpider(XMLFeedSpider):
    name = 'doi_gov'
    start_urls = ['https://www.doi.gov/feeds/list/11143/rss.xml',
                  'https://www.doi.gov/feeds/list/11142/rss.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = NewsRelease()
        item['title'] = node.xpath('title/text()').get()
        item['link'] = node.xpath('link/text()').get()
        item['source_id'] = 'DOI'
        item['summary'] = None
        item['content'] = None
        return item