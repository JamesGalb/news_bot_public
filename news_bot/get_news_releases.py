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
to_post_sql = "SELECT news_url, news_title FROM news WHERE reddit_post=0"
cursor.execute(to_post_sql)
data_to_post = cursor.fetchall()

#Checks for conditions and data to post to reddit
should_post_data = True
if len(sys.argv) > 1:
    should_post_data = sys.argv[1].lower() == 'true'
if should_post_data and len(data_to_post) > 0:

    #Logs into Reddit
    reddit = praw.Reddit(client_id='6DmZoP3phe8vYQ',
                           client_secret='UMVs6DYaXEgwBWOWiWWSCzliHAA',
                           password='********',
                           user_agent='PartyOfLions',
                           username='PartyOfLions') #reddit data in theses parentheses
                           
    #Pulls previous submissions from reddit, to compare DB reddit_posted to
    previous_submissions = reddit.redditor('PartyOfLions').submissions.new(limit=500)
    previous_links = []
    for sub in previous_submissions:
        previous_links.append(sub.url)

    #loops through and posts each entry in data_to_post
    for item in data_to_post:
        if(item[0] not in previous_links):
            item_list = [item[0], item[1]]
            ###Needs Regex here for capping posts to 297+"...", and removing after question marks (?) in URLs.
            if(" on Twitter: " in item_list[1]):
                item_list[1] = item_list[1].replace(" on Twitter: ", ": ", 1)
            if(len(item_list[1]) > 299):
                item_list[1] = item_list[1][:296] + '...'
            reddit.subreddit("Donald_Trump").submit(item_list[1], url=item_list[0])
            
            #Query DB to Update reddit_post
            update_reddit_sql = "UPDATE news SET reddit_post=1 WHERE news_url = %s"
            url_link = item[0]
            cursor.execute(update_reddit_sql, url_link)
            connection.commit()

else:
    print('Nothing New')
    
connection.close()
