from typing import Optional

from sqlmodel import Field

from data.models.base_model import BaseModel


class Character(BaseModel, table=True):
    __tablename__ = "characters"

    name: str = Field(nullable=False)
    height: float = Field(nullable=False)
    mass: float = Field(nullable=False)
    hair_color: str = Field(nullable=False)
    skin_color: str = Field(nullable=False)
    eye_color: str = Field(nullable=False)

    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
