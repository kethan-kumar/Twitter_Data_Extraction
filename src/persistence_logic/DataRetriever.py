from ..business_logic.CleaningData import CleaningData
from .MongoDB_DAO import MongoDB_DAO


class DataRetriever:

    def tweet_retriever(self):
        mongoDB_DAO = MongoDB_DAO("RawDb")
        collections = mongoDB_DAO.collections_list()
        print(collections)
        for collection_name in collections:
            print(collection_name)
            collection_list = []
            for record in mongoDB_DAO.retrieve_data(collection_name):
                clean_data = CleaningData()
                clean_data.clean_tweets(record)
                collection_list.append(record)
            self.save_cleaned_tweets(collection_list, collection_name)

    def save_cleaned_tweets(self, collection_list, collection_name):
        processed_db = MongoDB_DAO("ProcessedDb")
        processed_db.save_multiple_records(collection_list, collection_name)
