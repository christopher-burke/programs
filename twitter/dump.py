#!/usr/bin/env python3

"""Tweet status."""

from os import environ
import sys
import logging
import json

try:
    import tweepy
except ImportError:
    raise ImportError(f"Tweepy not installed, `pip install tweepy`.")


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='twitter.log',
                    filemode='a')


class TwitterAccount:
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

    def dump_tweets(self, twitter_account):
        """Tweet retrieve tweets from a twitter_account."""
        get_tweets = self.api.user_timeline

        try:
            tweets = get_tweets(screen_name=twitter_account,
                                count=200)
            logging.info(f':Retrived {len(tweets)} from {twitter_account}.')
        except Exception as e:
            logging.error(f'Something went wrong: \
                            dump_tweets(f{twitter_account}) Error:{e}.')
            return

        def get_more(last_tweet_id):
            more_tweets = get_tweets(screen_name=twitter_account,
                                     count=200,
                                     max_id=last_tweet_id)
            if more_tweets:
                return more_tweets
            return []
        more_tweets = True
        while more_tweets:
            more_tweets = get_more(tweets[-1].id)
            if len(more_tweets) > 0:
                tweets.extend(more_tweets)
            else:
                more_tweets = False
                break

        return tweets


if __name__ == "__main__":
    twitter_api = TwitterAccount()
