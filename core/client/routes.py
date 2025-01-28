from flask import Blueprint, render_template


client = Blueprint("client", __name__)


@client.route("/")
def home():
    return render_template("client/home.html")


@client.route("/about")
def about_us():
    return render_template('client/aboutus.html')