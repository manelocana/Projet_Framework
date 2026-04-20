

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


""" ici on inicialise la database, le login et les migrations """

db = SQLAlchemy()

login_manager = LoginManager()

migrate = Migrate()