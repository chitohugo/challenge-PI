import os

os.environ["ENV"] = "test"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

from app.core.security import get_password_hash
from data.models import *
from infrastructure.config import configs
from infrastructure.container import Container
from interface.main import AppCreator
from interface.schema.auth_schema import SignIn


@pytest.fixture(scope="session")
def engine():
    return create_engine(configs.DATABASE_URI)


@pytest.fixture(scope="session")
def tables(engine):
    SQLModel.metadata.create_all(engine)
    try:
        yield
    finally:
        SQLModel.metadata.drop_all(engine)


@pytest.fixture
def session(engine, tables):
    connection = engine.connect()
    session = Session(bind=connection)

    yield session

    session.rollback()
    connection.close()


@pytest.fixture
def client(session):
    app_creator = AppCreator()
    app = app_creator.app
    with TestClient(app) as client:
        yield client


@pytest.fixture
def create_user(session):
    data_user = {
        "email": "julian.clark@gmail.com",
        "username": "delicatesilk",
        "first_name": "Julian",
        "last_name": "Clark",
        "password": get_password_hash('dolor')
    }
    instance = User(**data_user)
    session.add(instance)
    session.commit()
    yield instance


@pytest.fixture
def container():
    return Container()


@pytest.fixture
def token(client, container):
    sign_in = SignIn(
        email="julian.clark@gmail.com",
        password="dolor"
    )

    service = container.auth_service
    response = service().sign_in(sign_in)
    yield response['access_token']


@pytest.fixture
def test_name(request):
    return request.node.name
