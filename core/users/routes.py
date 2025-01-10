from flask import Blueprint, render_template


users = Blueprint("users", __name__)


@users.route("/")
def home() -> str:
    return render_template("client/home.html")
