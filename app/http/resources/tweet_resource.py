from typing import Union, List
from app.models.tweet import Tweet
from app.http.resources.user_resource import UserResource


class TweetResource:
    def __init__(self, tweets: Union[Tweet, List[Tweet]]):
        if isinstance(tweets, list):
            if tweets is None:
                self.tweets = []
            else:
                self.tweets = [self._tweet_to_dict(tweet) for tweet in tweets]
        else:
            if tweets is None:
                self.tweet = {}
            else:
                self.tweet = self._tweet_to_dict(tweets)

    def _tweet_to_dict(self, tweet: Tweet):
        return {
            'id': tweet.id,
            'user_id': tweet.user_id,
            'user': UserResource(tweet.user).user,
            'tweet': tweet.tweet,
        }

    def __iter__(self):
        if hasattr(self, 'tweets'):
            for tweet in self.tweets:
                yield tweet
        else:
            yield self.tweet
