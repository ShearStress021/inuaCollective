from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class ProgramForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Create Program")


class SubProgramForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Sub Program")

class CommunityForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Program")


class YouthEmpowerMentForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Program")


class HousingForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Program")


class SportArtForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Program")


class BlogForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Blog")


class TestimonialForm(FlaskForm):
    name = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("Create Testimony")


class GalleryForm(FlaskForm):
    submit = SubmitField("Post Gallery")


# class OurTeam(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), unique=True, nullable=False)
#     profile_pic = db.Column(db.String(255), unique=True, nullable=False)
#     content = db.Column(db.Text,nullable=False)
#     linkedin_url = db.Column(db.String(255), nullable=True)
#     twitter_url = db.Column(db.String(255), nullable=True)
#     instagram_url = db.Column(db.String(255), nullable=True)
#     thread_url = db.Column(db.String(255), nullable=True)
#     facebook_url = db.Column(db.String(255), nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class OurTeamForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    content = TextAreaField("Profile Description", validators=[DataRequired()])
    linkedin_url = StringField("LinkedIn url")
    twitter_url = StringField("Twitter url")
    instagram_url = StringField("Instagram url")
    email_url = StringField("Email url")
    facebook_url = StringField("Facebook url")
    submit = SubmitField("Add Team Member")

