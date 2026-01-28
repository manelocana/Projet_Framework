

import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "DATABASE": ":memory:",   # SQLite in memory
        "WTF_CSRF_ENABLED": False # forms
    })

    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()
