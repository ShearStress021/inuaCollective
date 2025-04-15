from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import RegistrationForm, LoginForm, ProgramForm
from flask_login import current_user, login_user, login_required
from core.models import User, db, Program
from flask_bcrypt import Bcrypt
from .utils import create_path


bcrypt = Bcrypt()

users = Blueprint("users", __name__)


@users.route("/admin")
def home() -> str:
    return render_template("client/home.html")


@users.route("/admin/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("users.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.count() < 1:

            hash_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            admin = User(username=form.username.data, password=hash_password)
            db.session.add(admin)
            db.session.commit()
            flash(
                "Your account has been created! You are now able to log in", "success"
            )
            return redirect(url_for("users.home"))
    return render_template("register.html", form=form)


@users.route("/admin/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("users.home"))
    form = LoginForm()
    if form.validate_on_submit():
        admin = User.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("users.home"))
        else:
            flash("Login Unsuccessfull. Please check username and password", "danger")
    return render_template("login.html", title="login", form=form)


@users.route("/admin/program", methods=["GET", "POST"])
@login_required
def create_program():
    form = ProgramForm()
    if request.method == "POST":
        file = request.files["program_image"]
        if file:
            image_path = create_path("programs", file)
            program = Program(
                title=form.title.data,
                description=form.description.data,
                content=form.content.data,
                image_file=image_path,
                user_id=current_user.id,
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("users.home"))

    return render_template("create_program.html", form=form)
