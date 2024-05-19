from typing import Union, List
from app.models.user import User


class UserResource:
    def __init__(self, users: Union[User, List[User]]):
        if isinstance(users, list):
            self.users = [self._user_to_dict(user) for user in users]
        else:
            self.user = self._user_to_dict(users)

    def _user_to_dict(self, user: User):
        return {
            'id': user.id,
            'name': user.name,
            'identifier': user.identifier,
            'email': user.email,
            'description': user.description,
            'follower_count': len(user.followers),
            'following_count': len(user.following),
            'tweet_count': len(user.tweets),
            'tweets': user.tweets,
        }
