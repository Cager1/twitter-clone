from pydantic import BaseModel, SecretStr


class User(BaseModel):
    name: str
    email: str
    description: str = None
    identifier: str
    password: str
    password_confirmation: str


class UserRegister(BaseModel):
    name: str
    email: str
    password: str
    identifier: str = None
    password_confirmation: str


class UserLogin(BaseModel):
    email: str
    password: str
