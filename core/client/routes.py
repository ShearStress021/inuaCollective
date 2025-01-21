from flask import Blueprint, render_template


client = Blueprint("client", __name__)


@client.route("/")
def home():
    return render_template("client/home.html")
