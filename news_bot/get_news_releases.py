# -*- coding: utf-8 -*-
from news_releases.spider_runner import SpiderRunner
import logging
import praw
import sys
import pymysql


#Query DB for URL list, for spiders to check before adding items to Database
connection = pymysql.connect('localhost', 'bot', 'password', 'trump_news_bot')
cursor = connection.cursor()


#Run Spiders - Adds to Database in Pipeline
spider_runner = SpiderRunner()
spider_runner.run_spiders()


#Query DB for titles and links matching reddit_post:false, add to data_to_post
#to_post_sql = "SELECT news_url, news_title FROM news WHERE reddit_post=false"
#cursor.execute(to_post_sql)
#data_to_post = cursor.fetchall()


#Post data_to_post to Reddit
#should_post_data = True
#if len(sys.argv) > 1:
#    should_post_data = sys.argv[1].lower() == 'true'
#
#if should_post_data and len(data_to_post) > 0:
#    reddit = praw.Reddit(client_id='6DmZoP3phe8vYQ',
#                           client_secret='UMVs6DYaXEgwBWOWiWWSCzliHAA',
#                           password='********',
#                           user_agent='PartyOfLions',
#                           username='PartyOfLions') #reddit data in theses parentheses
#    previous_submissions = reddit.redditor('PartyOfLions').submissions.new(limit=500)
#    previous_links = []
#    for sub in previous_submissions:
#        previous_links.append(sub.url)
#    for link in data_to_post:
#        if(link['link'] not in previous_links):
#            reddit.subreddit("partyoflions").submit(link["title"], url=link["link"])
#            #Query DB to Update reddit_post
#            update_reddit_sql = "UPDATE trump_news_bot SET reddit_post = 1 WHERE news_url = %s"
#            cursor.execute(update_reddit_sql, (item['link']))
#    print('Success')
#else:
#    print('Nothing New')
                
connection.commit()
connection.close()