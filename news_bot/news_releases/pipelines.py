# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import time

class MySQLPipeline(object):

    def process_item(self, item, spider):
        connection = pymysql.connect('localhost', 'bot', 'password', 'trump_news_bot')
        cursor = connection.cursor()
        sql_insert = "INSERT IGNORE INTO `news`(`news_url`, `source_id`, `news_title`, `news_summary`, `news_content`) VALUES (%s,%s,%s,%s,%s)"
        values = (item['link'], item['source_id'], item['title'], item['summary'], item['content'])
        cursor.execute(sql_insert, values)
        connection.commit()
        connection.close()

        return item