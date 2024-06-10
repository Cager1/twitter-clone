from pydantic import BaseModel


class Tweet(BaseModel):
    id: int
    user_id: int
    tweet: str


class TweetStore(BaseModel):
    tweet: str
