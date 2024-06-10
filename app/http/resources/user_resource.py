from typing import Union, List
from app.models.user import User


class UserResource:
    def __init__(self, users: Union[User, List[User]]):
        if isinstance(users, list):
            if users is None:
                self.users = []
            else:
                self.users = [self._user_to_dict(user) for user in users]
        else:
            if users is None:
                self.user = {}
            else:
                self.user = self._user_to_dict(users)

    def _user_to_dict(self, user: User):
        return {
            'id': user.id,
            'name': user.name,
            'identifier': user.identifier,
            'email': user.email,
            'description': user.description,
            'followers': [follower.follower.name for follower in user.followers],
            'following': [following.user.name for following in user.following],
            'follower_count': len([follower.follower.name for follower in user.followers]),
            'following_count': len([follower.follower.name for follower in user.following]),
            'tweet_count': len([tweet for tweet in user.tweets]),
            'tweets': [tweet.tweet for tweet in user.tweets],
        }

    def __iter__(self):
        if hasattr(self, 'users'):
            for user in self.users:
                yield user
        else:
            yield self.user
