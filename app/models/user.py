from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    email: str
    description: str = None
    identifier: str
    password: str
    password_confirmation: str

class UserRegister(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    identifier: str = None
    password_confirmation: str = Field(...)


class UserLogin(BaseModel):
    email: str
    password: str
