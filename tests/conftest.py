

import os
import tempfile
import pytest
from app.extensions import db as _db
from main import create_app
from flask import Flask

from app.models.user import User


# app flask pour tests, avec sqlite temporel
@pytest.fixture(scope="session")
def app():
    # fichier temporel
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # faire les tables
    with app.app_context():
        _db.create_all()

    yield app

    # fermer et effacer le db temporel
    os.close(db_fd)
    os.unlink(db_path)



@pytest.fixture(scope="function")
def client(app):
    # return le client de test flask
    return app.test_client()



@pytest.fixture(scope="function")
def admin_user(session):
    # si admin deja dans db, on delete pour creer un nouveau
    session.query(User).filter_by(username="admin").delete()
    session.commit()

    user = User(username="admin", password="1234", role="admin")
    session.add(user)
    session.commit()
    return user





@pytest.fixture(scope="function")
def session(app):
    # on utilise session par defect in db
    with app.app_context():
        connection = _db.engine.connect()
        transaction = connection.begin()

        _db.session.begin_nested()  # abrir transacción anidada

        yield _db.session  # session pour le test

        _db.session.rollback()  # rollback -> nettoyer
        transaction.rollback()
        connection.close()
