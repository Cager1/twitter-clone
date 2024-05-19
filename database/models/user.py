from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    identifier = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    hashed_password = Column(String(255), nullable=False)

    followers = relationship("Follower", back_populates="user", foreign_keys="Follower.user_id")
    # following relation that hits the Follower table on column follower_id
    following = relationship("Follower", back_populates="follower", foreign_keys="Follower.follower_id")
    tweets = relationship("Tweet", back_populates="user")

