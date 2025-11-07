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
