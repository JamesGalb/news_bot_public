# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    start_urls = ['https://twitter.com/teamtrump',
                  'https://twitter.com/realDonaldTrump',
                  'https://twitter.com/WhiteHouse']

    def parse(self, response):
        items = []
        for element in response.css('ol#stream-items-id li div.tweet')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['link'] = 'https://www.twitter.com' + element.css('::attr(data-permalink-path)').extract_first()
            item['source_id'] = 'TWR'
            item['summary'] = None
            item['content'] = None
            request = scrapy.Request(item['link'], callback=self.parse_retweet)
            request.meta['item'] = item
            items.append(request)
        return items

    def parse_retweet(self, response):
        item = response.meta['item']
        item['title'] = response.css('title::text').extract_first()[:299]
        return item
