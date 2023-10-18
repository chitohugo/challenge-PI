import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings
from fastapi import Query
from fastapi_pagination import Page

load_dotenv()

ENV: str = ""


class Configs(BaseSettings):
    # BASE
    ENV: str = os.getenv("ENV", "dev")
    API: str = "/api"
    PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Challenge-Pi"
    ENV_DATABASE: dict = {
        "dev": "challenge",
        "test": "challenge-test",
    }
    ENGINES: dict = {
        "sqlite": "sqlite:///"
    }

    # DATE
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # AUTH
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # DATABASE
    DATABASE_NAME = ENV_DATABASE[ENV]
    ENGINE = ENGINES.get(os.getenv("ENGINE"))
    DATABASE_URI = f"{ENGINE}{DATABASE_NAME}.db"

    # PAGINATION
    Page = Page.with_custom_options(
        size=Query(30, ge=1, le=50),
    )

    class Config:
        case_sensitive = True


class TestConfigs(Configs):
    ENV: str = "test"


configs = Configs()

if ENV == "prod":
    pass
elif ENV == "stage":
    pass
elif ENV == "test":
    setting = TestConfigs()
