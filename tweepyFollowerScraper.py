from __future__ import print_function
from __future__ import with_statement
import tweepy
import time
import pickle

#setup a twitter app and add credentials below
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#choose account to scrape followers from
target_twitter_account = ''

#authenticate with twitter api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
print ("authed")

followerIDs = []
pages = tweepy.Cursor(api.followers_ids, id= target_twitter_account, stringify_ids=True).pages()
while True:
    try:
        page = pages.next()
        followerids.extend(page)
    except tweepy.TweepError:
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break

print ('writing to file')
with open('twitterIDs.txt', 'a') as f:
    for twid in followerids:
    	f.write(twid+'\n') 
print ('done')
