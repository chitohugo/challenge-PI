from typing import Optional

from pydantic import BaseModel

from interface.schema.base_schema import ModelBaseInfo


class BaseCharacter(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str

    class Config:
        orm_mode = True


class Character(ModelBaseInfo, BaseCharacter):
    ...


class PostCharacter(BaseCharacter):
    user_id: Optional[int]
    ...


class UpdateCharacter(BaseCharacter):
    ...
