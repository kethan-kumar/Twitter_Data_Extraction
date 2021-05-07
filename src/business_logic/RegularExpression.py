import re


def regular_expression(tweet_to_clean):
    cleaned_tweet = re.findall("([\w\s])", tweet_to_clean)
    cleaned_tweet = ''.join(cleaned_tweet)
    cleaned_tweet = re.sub("_", "", cleaned_tweet)
    cleaned_tweet = re.sub("([\n])", "", cleaned_tweet)
    cleaned_tweet = re.sub('http | https\S+', "", cleaned_tweet)
    cleaned_tweet = re.sub("([\s]{2,})", " ", cleaned_tweet)

    return cleaned_tweet
