import tweepy
from tweepy import Cursor

from AuthenticationMechanism import AuthenticationMechanism
from src.persistence_logic.MongoDB_DAO import MongoDB_DAO


class TwitterSearchAPI:

    def __init__(self):
        self.auth = AuthenticationMechanism.authentication()
        self.api = tweepy.API(self.auth)
        self.search_keywords = ["Storm", "Winter", "Canada", "Temperature", "Flu", "Snow", "Indoor", "Safety"]
        self.mongoDb_DAO = MongoDB_DAO("RawDb")

    def twitter_search_api_tweets(self):
        for word in self.search_keywords:
            iterator = 0
            tweets = []
            search_tweets_cursor = Cursor(self.api.search, q=word, lang="en").items(270)
            for tweet in search_tweets_cursor:
                iterator = iterator + 1
                tweets.append(tweet._json)
            self.mongoDb_DAO.save_multiple_records(tweets, "Twitter_Search_Collection")
