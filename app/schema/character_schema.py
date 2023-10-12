from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo


class BaseCharacter(BaseModel):
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
    user_id: int

    class Config:
        orm_mode = True


class Character(ModelBaseInfo, BaseCharacter):
    ...
