from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
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
