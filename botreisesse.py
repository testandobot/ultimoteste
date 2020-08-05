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
conta = 0
contar = 0
textos = ["\"A esperança vencerá o medo\"\nManda salve pro 3S, melhor presidente de todos os tempos!", "Manda salve pro 3s2, Presidente @LulaOficial", "O MELHOR PRESIDENTE DE TODOS OS TEMPOS\nManda salve pro 3S2, @LulaOficial"]
print(api.me())
print(str(len(textos)))

if __name__ == "__main__":
    while True:
        class MyStreamListener(tweepy.StreamListener):
            def on_status(self, status):
                global conta
                global contar
                if status.user.screen_name == "LulaOficial" and not "RT" in status.text:
                    try:
                        if conta > len(textos):
                            conta = 0
                        api.update_status(textos[conta], in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                        api.create_favorite(status.id)
                        api.retweet(status.id)
                        conta += 1
                    except tweepy.TweepError as e:
                        print(e.reason)
                else:
                    print(status.text)
                #   contar += 1
                #   if contar % 5:
                #     print("N")
                  
            
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(follow=["2670726740"])
