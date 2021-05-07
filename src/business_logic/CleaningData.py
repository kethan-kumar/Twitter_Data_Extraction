from RegularExpression import regular_expression


class CleaningData:

    def clean_tweets(self, tweets):
        for key in tweets.keys():
            if type(tweets.get(key)) == str and (key != 'created_at'):
                tweets[key] = regular_expression(tweets.get(key))

            elif type(tweets.get(key)) == dict:
                self.clean_tweets(tweets.get(key))
