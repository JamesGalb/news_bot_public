# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class HUDGovSpider(scrapy.Spider):
    name = 'hud_gov'
    custom_settings = {'EXPECTED': 9}
    start_urls = ['https://www.hud.gov/press/speeches_remarks_statements',
                  'https://www.hud.gov/press/press_releases_media_advisories',
                  'https://www.hud.gov/press/testimonies']

    def parse(self, response):
        items = []
        for element in response.css('div.col-md-12 p a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.hud.gov" + element.css('::attr(href)').extract_first()
            item['source_id'] = 'HUD'
            item['summary'] = None
            item['content'] = None
            items.append(item)
        return items
