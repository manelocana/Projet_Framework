

from flask_login import UserMixin
from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash



""" LES MODELS SONT LES TABLES DANS MYSQL """


""" table pour mysql """
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), server_default='user', nullable=False)

    """ relation user avec post/projects """
    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")
    projects = db.relationship('Project', backref='author', lazy=True, cascade="all, delete-orphan")


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
