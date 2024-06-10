import json

from app.http.resources.tweet_resource import TweetResource
from app.models.user import User
from config.kafka import produce_tweet
from database.connection import db
from database.models.tweet import Tweet


# function that returns random tweets
async def index(user: User = None):
    # get all tweets from the database and limit them to 10
    tweets = db.query(Tweet).limit(10).all()
    for tweet in tweets:
        # serialize the tweet data to JSON
        tweet_json = json.dumps(TweetResource(tweet).tweet)

        # send the tweet data to the Kafka topic
        await produce_tweet(tweet_json)
    return TweetResource(tweets)


# when new tweet is created, send it to the Kafka topic
async def store(tweet, user):
    # add the tweet to the database
    db_tweet = Tweet(
        user_id=user.id,
        tweet=tweet.tweet
    )
    db.add(db_tweet)
    db.commit()
    # get the tweet from the database
    db_tweet = db.query(Tweet).filter(Tweet.id == db_tweet.id).first()

    # serialize the tweet data to JSON
    tweet_json = json.dumps(TweetResource(db_tweet).tweet)

    # send the tweet data to the Kafka topic
    await produce_tweet(tweet_json)
    return TweetResource(db_tweet)



