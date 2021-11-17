import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app as main_app
from src.config import environment
from src.config import mongo_settings
from src.mongo_client import MongoDBClient

TEST_DB_NAME = 'tfg_testing_db'


@pytest.fixture
def app() -> FastAPI:
    return main_app


@pytest.fixture
def app_client(app) -> TestClient:  # noqa: WPS442
    return TestClient(app)


@pytest.fixture
def mongo_client():
    with MongoDBClient(uri=mongo_settings.uri, database=TEST_DB_NAME) as db_client:
        yield db_client
        db_client.drop_test_database(TEST_DB_NAME)


@pytest.fixture
def secret_key():
    return environment.secret_key
