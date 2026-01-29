

import pytest
from app import create_app
from app.extensions import db

@pytest.fixture
def app():
    app = create_app()

    # Configuración SOLO para tests
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "LOGIN_DISABLED": True,  # evita problemas con login_required
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()








from app.models.user import User
from app.extensions import db

@pytest.fixture
def admin_user(app):
    user = User(
        username="admin",
        password="1234"
    )
    db.session.add(user)
    db.session.commit()
    return user
