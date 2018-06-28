#!/usr/bin/env python3

"""Tweet status."""

from os import environ
import sys
import logging

try:
    import tweepy
except ImportError:
    raise ImportError(f"Tweepy not installed, `pip install tweepy`.")


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='twitter.log',
                    filemode='a')


class TwitterAccount():
    """Access to Twitter account using tweepy."""

    CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY')
    ACCESS_TOKEN = environ.get('TWITTER_ACCESS_TOKEN')
    CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET')
    ACCESS_SECRET = environ .get('TWITTER_ACCESS_SECRET')

    def __init__(self):
        """Access twitter account with tweepy."""
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def tweet_status(self, tweet):
        """Tweet status."""
        try:
            self.api.update_status(tweet)
            logging.info(f'Tweet Posted: {tweet}.')
        except Exception as e:
            logging.error(f'Something went wrong: {e}. Tweet: {tweet}.')


if __name__ == "__main__":
    twitter_api = TwitterAccount()
    twitter_api.tweet_status(sys.argv[1])
