# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class YoutubeSpider(scrapy.Spider):
    name = 'youtube'
    custom_settings = {'EXPECTED': 18}
    start_urls = ['https://www.youtube.com/user/whitehouse/videos',
                  'https://www.youtube.com/user/statevideo/videos',
                  'https://www.youtube.com/user/rnc/videos',
                  'https://www.youtube.com/user/GOPICYMI/videos',
                  'https://www.youtube.com/channel/UCADso8k7tSZT3HpD4ZK3W9Q/videos',
                  'https://www.youtube.com/channel/UCAql2DyGU2un1Ei2nMYsqOA/videos']

    def parse(self, response):
        items = []
        for element in response.css('h3.yt-lockup-title a.yt-uix-tile-link')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            if('UCAql2DyGU2un1Ei2nMYsqOA' in response.url):
                item['title'] = '**TRUMP TV** ' + element.css('::text').extract_first()
            else:
                item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.youtube.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
