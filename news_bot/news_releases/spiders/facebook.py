# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class FacebookSpider(scrapy.Spider):
    name = 'facebook'
    start_urls = ['https://mobile.facebook.com/DonaldTrump/']

    def parse(self, response):
        items = []
        for element in response.css('div#recent div.em.en div.eo.ep.eq div.dj.er.es')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('div.et div.fb span p::text').extract_first()[:299]
            item['link'] = "https://www.facebook.com" + element.css('div.fo div.cp span.cp a.ft::attr(href)').extract_first()
            if (item['title'] == ""):
                item['title'] = "Donald Trump Facebook Post"
            items.append(item)
        return items
