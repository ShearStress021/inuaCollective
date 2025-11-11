import uuid

from sqlalchemy.exc import OperationalError
from flask_login import UserMixin
from core.extensions import login_manager, db





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
    
    communitys = db.relationship("Community", backref="user", lazy=True)
    youthEmpowerments = db.relationship("YouthEmpowerMent", backref="user", lazy=True)
    housings = db.relationship("Housing", backref="user", lazy=True)
    sportsarts = db.relationship("SportsArt", backref="user", lazy=True)
    gallerys = db.relationship("Gallery", backref="user", lazy=True)
    blogs = db.relationship("Blog", backref="user", lazy=True)
    testimonials = db.relationship("Testimonial", backref="user", lazy=True)
    events = db.relationship("Event", backref="user", lazy=True)
    ourTeams = db.relationship("OurTeam", backref="user", lazy=True)
    programs = db.relationship("Program", backref="user", lazy=True)
    subprograms = db.relationship("SubProgram", backref="user", lazy=True)

    def __repr__(self):
        return f"User({self.username})"

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Fixed backref - now you can do: subprogram.program
    subprograms = db.relationship("SubProgram", backref="program", lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Program('{self.title}')"

class SubProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)  # Removed unique=True
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), nullable=False)  # Removed unique=True
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  # Added
    
    # Ensure title is unique PER program (not globally)
    __table_args__ = (
        db.UniqueConstraint('title', 'program_id', name='unique_subprogram_per_program'),
    )
    
    def __repr__(self):
        return f"SubProgram('{self.title}')"


class Community(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)  
    
    def __repr__(self):
        return f"SubProgram ({self.title})"
class YouthEmpowerMent(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"SubProgram ({self.title})"

class Housing(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
   
    def __repr__(self):
        return f"SubProgram ({self.title})"

class SportsArt(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"SubProgram ({self.title})"




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
