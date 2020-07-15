import os
import tweepy
import time
import datetime
from os import environ

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
                if status.user.screen_name == "3s_of" and not "RT" in status.text:
                    try:
                     api.create_favorite(status.id)
                     api.retweet(status.id)
                    except tweepy.TweepError as e:
                     print(e.reason)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=["1274460778205151232"])

while True:
    for i in range(20):
        api.update_status("tweet nº: " + i)
        time.sleep(30)