from flask import Flask
from .users.routes import users


def create_app() -> None:
    app = Flask(__name__)
    app.register_blueprint(users)

    return app
