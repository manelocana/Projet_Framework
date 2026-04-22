

from flask import Flask
from config import Config
from app.extensions import db, login_manager, migrate

from app.public.routes.home import home_bp
from app.public.routes.pages import pages_bp
from app.public.routes.portfolio import portfolio_bp
from app.public.routes.blog import blog_bp
from app.public.routes.contact import contact_bp

from app.admin.routes.auth import auth_bp
from app.admin.routes.admin_routes import admin_bp
from app.admin.routes.auth_register import auth_register_bp
from app.admin.routes.blog_admin import blog_admin_bp
from app.admin.routes.portfolio_admin import portfolio_admin_bp
from app.admin.routes.pages_admin import pages_admin_bp

from app.user.routes.user_routes import user_bp


import pymysql



pymysql.install_as_MySQLdb()



def create_app(config_class=Config):
    app = Flask(__name__)

    """ configuration depuis la class Config """
    app.config.from_object(config_class)

    # CSRFProtect(app)

    """ inicialiser la database et regarder si a des migrations """
    db.init_app(app)
    migrate.init_app(app, db)
    
    """ inicialiser le login """
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    """ registrer les blueprint qui contient les routes """
    app.register_blueprint(home_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(contact_bp)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    app.register_blueprint(blog_admin_bp)
    app.register_blueprint(portfolio_admin_bp)
    app.register_blueprint(auth_register_bp)
    app.register_blueprint(pages_admin_bp)

    app.register_blueprint(user_bp)


    return app
