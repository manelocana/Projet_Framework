

import pytest
from app import create_app
from app.extensions import db as _db
from app.models.user import User
from app.models.post import Post

from config import TestConfig



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
    u = User(username="testuser", password="1234")
    db.session.add(u)
    db.session.commit()
    return u



# Fixture de un post de prueba
@pytest.fixture
def post(db, user):
    p = Post(title="Test Post", description="Holaaaa", user=user)
    db.session.add(p)
    db.session.commit()
    return p



@pytest.fixture
def admin_user(db):

    existing = db.session.query(User).filter_by(username="admin").first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        
    u = User(username="admin", password="1234", role="admin")
    db.session.add(u)
    db.session.commit()
    return u

