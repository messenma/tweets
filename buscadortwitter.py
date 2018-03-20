import os
import tweepy
from textblob import TextBlob

consumer_key = '7CxQnQBvRuCp2X8daDdv3qKsb'
consumer_secret = 'RNgZY5zm2VMK5ymv7RP2c3jr8gGpQpkORlsaBFTx0WHxoYUq0V'
access_token = '135335612-v9SgiGkUsApA8aRocluYR7V9XiXCnlG2DUVvT8Su'
access_token_secret = 'xszmOMB7NVajW84y95ofecl9KAoL2pOoViueUAob6cnA4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('coca-cola')


for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


	