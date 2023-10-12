from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo


class BaseUser(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class User(ModelBaseInfo, BaseUser):
    ...


class UpsertUser(BaseUser):
    ...
