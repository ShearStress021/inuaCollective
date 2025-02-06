from flask import Blueprint, render_template
from ..models import Program

client = Blueprint("client", __name__)


@client.route("/")
def home():
    return render_template("client/home.html")


@client.route("/about")
def about_us():
    return render_template("client/aboutus.html")


@client.route("/programs")
def program():
    programs = Program.query.all()

    return render_template("client/program.html", programs=programs)
