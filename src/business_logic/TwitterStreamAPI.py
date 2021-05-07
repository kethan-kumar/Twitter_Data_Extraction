from tweepy import Stream

from AuthenticationMechanism import AuthenticationMechanism
from TwitterLiveStreamAccess import TwitterLiveStreamAccess


class TwitterStreamAPI:

    def __init__(self):
        self.number_of_tweets_to_fetch = 2000
        self.twitter_stream_listener = TwitterLiveStreamAccess(self.number_of_tweets_to_fetch)
        authentication = AuthenticationMechanism()
        self.auth = authentication.authentication()
        self.stream = Stream(self.auth, self.twitter_stream_listener)
        self.search_keywords = ["Storm", "Winter", "Canada", "Flu", "Snow", "Indoor", "Safety", "Temperature"]

    def twitter_stream_api_tweets(self):
        self.recursive_stream_call()
        stream_tweets = self.twitter_stream_listener.live_stream_data
        self.twitter_stream_listener.mongoDb_DAO.save_multiple_records(stream_tweets, "Twitter_Stream_Collection")

    def recursive_stream_call(self):
        self.stream.filter(track=self.search_keywords, languages=["en"])
        if self.twitter_stream_listener.counter < self.number_of_tweets_to_fetch:
            self.recursive_stream_call()
