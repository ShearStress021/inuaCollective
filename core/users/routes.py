from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import RegistrationForm, LoginForm, ProgramForm, BlogForm, TestimonialForm
from flask_login import current_user, login_user, login_required, logout_user
from core.models import User, db, Program, Blog, Testimonial
from flask_bcrypt import Bcrypt
from .utils import create_path


bcrypt = Bcrypt()

users = Blueprint("users", __name__)

# admin section


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
            return redirect(url_for("users.program"))
    return render_template("register.html", form=form)


@users.route("/admin/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("users.create_program"))
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
                content=form.content.data,
                image_file=image_path,
                user_id=current_user.id,
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("users.program"))

    return render_template("create_program.html", form=form)


@users.route("/admin/blog", methods=["GET", "POST"])
@login_required
def create_blog():
    form = BlogForm()
    if request.method == "POST":
        file = request.files["blog_image"]
        if file:
            image_path = create_path("blog", file)
            blog = Blog(
                title=form.title.data,
                content=form.content.data,
                image_file=image_path,
                user_id=current_user.id,
            )
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for("users.blog"))
    return render_template("create_blog.html", form=form)


@users.route("/admin/testimonial", methods=["GET", "POST"])
@login_required
def create_testimonial():
    form = TestimonialForm()
    if request.method == "POST":
        file = request.files["profile_image"]
        if file:
            image_path = create_path("blog", file)
            testimony = TestimonialForm(
                title=form.name.data,
                content=form.content.data,
                profile_pic=image_path,
                user_id=current_user.id,
            )
            db.session.add(testimony)
            db.session.commit()
            return redirect(url_for("users.blog"))
    return render_template("create_testimonial.html", form=form)


@users.route("/admin/logout")
def log_out():
    logout_user()
    return redirect(url_for("users.home"))


# users view


@users.route("/")
def home():
    program = Program.query.first()
    return render_template("home.html", program=program)


@users.route("/programs")
def program():
    programs = Program.query.all()
    return render_template("program.html", programs=programs)


@users.route("/gallery")
def gallery():
    return render_template("gallery.html")


@users.route("/about")
def about():
    return render_template("about.html")


@users.route("/blog")
def blog():
    blogs = Blog.query.all()
    return render_template("blog.html", blogs=blogs)


@users.route("/event")
def event():
    return render_template("event.html")


@users.route("/program/<int:program_id>")
def program_detail(program_id):
    program = Program.query.get_or_404(program_id)
    return render_template("program_detail.html", program=program)
