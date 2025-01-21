from flask import Flask
from .users.routes import users, bcrypt
from .client.routes import client
from .config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from core.models import db, login_manager


login_manager.login_view = "users.login"


def create_app(app) -> None:
    app.config.from_object(Config)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)

    create_db(app)
    app.register_blueprint(users)
    app.register_blueprint(client)

    return app


def create_db(app):
    with app.app_context():
        db.create_all()
