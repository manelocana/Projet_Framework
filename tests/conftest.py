

import pytest
from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False



@pytest.fixture
def app():
    app = create_app(config_class=TestConfig)
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()
