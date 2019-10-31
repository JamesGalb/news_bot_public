import requests
import io
import os
import praw
import json
import logging
import pdb
def load_data():
    data_file = io.open(os.path.join(os.path.dirname(__file__), 'livestream_data.txt'), 'r', encoding='utf-8')
    line = data_file.readline()
    data_file.close()
    if(line == u''):
        return []
    else:
        return json.loads(line)

def set_data(data):
    if(len(data) > 0):
        data_file = io.open(os.path.join(os.path.dirname(__file__), 'livestream_data.txt'), 'w', encoding='utf-8')
        data_file.write(json.dumps(data, ensure_ascii=False))
        data_file.close()

channels = ["UCYxRlFDqcWM4y7FfpiAN3KQ", #whitehouse
            "UCpuofAxlrUAgnu7QEwKQwxw", #DODvClips
            "UC6ZhpmNnLxlOYipqh8wbM3A"] #statevideo
posted = load_data() #post_id, stream_id
streaming = [] #stream_id
to_post = [] #stream_id, title
to_unsticky = [] #post_id, stream_id

for channel in channels:
    request = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=' + channel + '&eventType=live&type=video&key=AIzaSyAQqICMDGo3j0Sfqp3iNpNrJdHjEgi0hBU')
    for stream in request.json()['items']:
        stream_id = stream['id']['videoId']
        streaming.append(stream_id)
        if(not any(post['stream_id'] == stream_id for post in posted)):
            to_post.append({'stream_id': stream_id, 'title': stream['snippet']['title']})

for post in posted:
    if(post['stream_id'] not in streaming):
        to_unsticky.append(post)

if len(to_post) > 0 or len(to_unsticky) > 0:
    reddit = praw.Reddit(client_id='6DmZoP3phe8vYQ',
                           client_secret='UMVs6DYaXEgwBWOWiWWSCzliHAA',
                           password='********',
                           user_agent='PartyOfLions',
                           username='PartyOfLions') #reddit data in theses parentheses
    for post_data in to_post:
        post = reddit.subreddit("partyoflions").submit(post_data["title"], url='https://www.youtube.com/watch?v=' + post_data['stream_id'])
        post.mod.sticky()
        post.mod.flair(text='LIVE!', css_class='live-flair')
        posted.append({'post_id': post.id, 'stream_id': post_data['stream_id']})
    for post_to_unsticky in to_unsticky:
        try:
            #using the word submission because this post is already on reddit
            submission_to_unsticky = reddit.submission(post_to_unsticky['post_id'])
            submission_to_unsticky.mod.sticky(state=False)
            submission_to_unsticky.mod.flair(text=None, css_class=None)
        except Exception:
            logging.error("Error when trying to unsticky post. (Doesn't exist?)")
        posted.remove(post_to_unsticky)

set_data(posted)
