from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.base import Base


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tweet = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tweets')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Tweet {self.tweet_id}>'
