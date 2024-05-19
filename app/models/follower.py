from pydantic import BaseModel, SecretStr


class Follower(BaseModel):
    user_id: int
    follower_id: int
