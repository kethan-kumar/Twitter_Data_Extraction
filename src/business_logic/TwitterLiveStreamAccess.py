import json

from tweepy import StreamListener

from CleaningData import CleaningData
from src.persistence_logic.MongoDB_DAO import MongoDB_DAO


class TwitterLiveStreamAccess(StreamListener):

    def __init__(self, tweet_retrieve_limit):
        super().__init__()
        self.counter = 0
        self.tweet_retrieve_limit = tweet_retrieve_limit
        self.cleaning_data = CleaningData()
        self.mongoDb_DAO = MongoDB_DAO("RawDb")
        self.live_stream_data = []

    def on_data(self, live_data):
        self.counter = self.counter + 1
        stream_tweets = json.loads(live_data)
        self.live_stream_data.append(stream_tweets)
        if self.counter > self.tweet_retrieve_limit:
            return False
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False
