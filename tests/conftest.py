

import pytest
from app import create_app
from app.extensions import db as _db
from app.models.user import User
from app.models.post import Post

from config import TestConfig
import uuid


@pytest.fixture
def login(client):

    def do_login(user):
        with client.session_transaction() as sess:
            sess["_user_id"] = str(user.id)
            sess["_fresh"] = True

    return do_login




@pytest.fixture(autouse=True)
def reset_login_state(app):
    with app.app_context():
        from flask import g
        g.pop('_login_user', None)
    yield
    with app.app_context():
        from flask import g
        g.pop('_login_user', None)



# Fixture de la app
@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig)
    
    with app.app_context():
        _db.create_all()  # Crear tablas en memoria
        yield app
        _db.session.remove()
        _db.drop_all()  # Limpiar DB al final



# Fixture del client de Flask para hacer request
@pytest.fixture
def client(app):
    return app.test_client()


# Fixture de la base de datos (transacciones por test)
# cuando modificamos la db
@pytest.fixture(scope="function")
def db(app):

    _db.session.begin_nested()

    yield _db

    _db.session.rollback()


# Fixture de un usuario de prueba, role=user
# test de rutas admin
@pytest.fixture
def user(db):
    unique_name = f"testuser_{uuid.uuid4().hex}"

    u = User(username=unique_name)
    u.set_password("1234")

    db.session.add(u)
    db.session.commit()

    return u



# Fixture de un post de prueba
@pytest.fixture
def post(db, user):
    p = Post(title="Test Post", description="testing pour post", author=user)
    db.session.add(p)
    db.session.commit()
    return p



@pytest.fixture
def admin_user(db):

    unique_name = f"admin_{uuid.uuid4().hex}"

    u = User(
        username=unique_name,
        role="admin"
    )

    u.set_password("1234")

    db.session.add(u)
    db.session.commit()

    return u
