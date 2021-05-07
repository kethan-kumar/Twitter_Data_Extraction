from src.business_logic.TwitterSearchAPIr import TwitterSearchAPI
from src.business_logic.TwitterStreamAPI import TwitterStreamAPI
from src.persistence_logic.DataRetriever import DataRetriever

if __name__ == '__main__':
    print("Twitter Search API initialization and extraction ...")
    twitter_extractor = TwitterSearchAPI()
    twitter_extractor.twitter_search_api_tweets()

    print("Twitter Stream API initialization and extraction ...")
    twitter_stream_extractor = TwitterStreamAPI()
    twitter_stream_extractor.twitter_stream_api_tweets()

    print("Twitter data extraction and save point ...")
    data_retriever = DataRetriever()
    data_retriever.tweet_retriever()
