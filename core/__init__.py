from flask import Flask
from .users.routes import users, bcrypt

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
    app.jinja_env.filters["truncatewords"] = truncate_words

    return app


def create_db(app):
    with app.app_context():
        db.create_all()


def truncate_words(s, num_words) -> str:
    words = s.split()
    return " ".join(words[:num_words]) + (" ..." if len(words) > num_words else "")
