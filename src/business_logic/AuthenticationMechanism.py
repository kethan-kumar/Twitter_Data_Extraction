import tweepy

from src.configuration import TwitterCredentials


class AuthenticationMechanism:

    @staticmethod
    def authentication():
        credential_authentication = tweepy.OAuthHandler(TwitterCredentials.consumer_key,
                                                        TwitterCredentials.consumer_secret)
        credential_authentication.set_access_token(TwitterCredentials.access_key, TwitterCredentials.access_secret)
        return credential_authentication
