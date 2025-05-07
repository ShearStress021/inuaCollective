import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from flask_login import LoginManager, UserMixin


db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except OperationalError:
        return None


def generate_uuid():
    return str(uuid.uuid4())


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    programs = db.relationship("Program", backref="user", lazy=True)
    programs = db.relationship("Gallery", backref="user", lazy=True)
    programs = db.relationship("Blog", backref="user", lazy=True)
    programs = db.relationship("Testimonial", backref="user", lazy=True)
    programs = db.relationship("Event", backref="user", lazy=True)
    programs = db.relationship("OurTeam", backref="user", lazy=True)

    def __repr__(self):
        return f"User({self.username})"


class Program(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Program ({self.title})"


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Blog ({self.title})"


class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    profile_pic = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Testimonial ({self.name})"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    link = db.Column(db.String(255), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class OurTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    profile_pic = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
