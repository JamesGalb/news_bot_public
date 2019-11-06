# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class HHSGovBlogSpider(scrapy.Spider):
    name = 'hhs_gov_blog'
    start_urls = ['https://www.hhs.gov/blog']

    def parse(self, response):
        items = []
        for element in response.css('div.blog-post-row div.node-internal-blog-post div.group-header div div.field-items div a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('::attr(href)').extract_first()
            item['source_id'] = 'HHS'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
