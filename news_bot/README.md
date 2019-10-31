# news-scraper

#### pre-reqs
  * python 3.8
  * sudo apt-get install python-setuptools
  * pip install praw
  * pip install scrapy


Run get_news_releases.py on a schedule to get new data

To scrape without posts, run 'python get_news_releases.py false'
The second argument, which defaults to true, decides whether the found links should be posted.

In order to use, you will have to create your own praw.ini or supply the correct arguments for praw.Reddit()
