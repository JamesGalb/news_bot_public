# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from get_news_releases import current_url_list

class MySQLPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect('localhost', 'bot', 'password', 'trump_news_bot')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):   
        if any(self.item['link'] in URL for URL in current_url_list):
            pass
        else:
            sql_insert = "INSERT IGNORE INTO news (news_url, source_id, news_title, news_summary, news_content, reddit_post) VALUES (%s, %s, %s, %s, %s, 0)"
            self.cursor.execute(sql_insert, (item['link'], item['source_id'], item['title'], item['summary'], item['content']))
        return item