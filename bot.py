import tweepy


import tweepy
import time

auth = tweepy.OAuthHandler('ohH2H1Icz2BIyPQQF5Yx3w7gF','QGxgTQgC8EvJUqWvvZStqepEUDNcDLTeLidixAKHrPHMPnYe0W')
auth.set_access_token('1292552542736592897-n8OTSRcAJ2vByJrTGFYfx5burXXLZ1','3Dt9iIWwQIi5rJbvxpwlB1JYx1KrKWbLuytiFb5bttaeD')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True )

user = api.me()

search = 'teu cu'
nmrdt = 2400

for tweet in tweepy.Cursor(api.search, search).items(nmrdt):
    try:
        api.update_status("nosso cu", in_reply_to_status_id=tweet.id)
        print('tweet retuitado e favoritado')
        tweet.retweet()
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break