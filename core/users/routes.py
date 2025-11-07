from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from .forms import (
    RegistrationForm,
    GalleryForm,
    LoginForm,
    CommunityForm,
    HousingForm,
    SportArtForm,
    YouthEmpowerMentForm,
    BlogForm,
    TestimonialForm,
)
from flask_login import current_user, login_user, login_required, logout_user
from core.models import (
    User, 
    db, 
    Blog, 
    Testimonial, 
    Gallery,
    Community,
    Housing,
    SportsArt,
    YouthEmpowerMent)
from core.extensions import bcrypt
from .utils import create_path



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




@users.route("/admin/program/<int:program_id>/delete", methods=["POST"])
@login_required
def delete_program(program_id):
    program = Program.query.get_or_404(program_id)
    if program.user != current_user:
        abort(403)
    db.session.delete(program)
    db.session.commit()
    return redirect(url_for("users.program"))

@users.route("/admin/community_program", methods=["GET", "POST"])
@login_required
def create_community_program():
    form = CommunityForm()
    if request.method == "POST":
        file = request.files["subprogram_image"]
        if file:
            image_path = create_path("community",file)
            program = Community(
                    title = form.title.data,
                    content=form.content.data,
                    image_file=image_path,
                      user_id=current_user.id,
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("users.community_program"))

    return render_template("create_community.html", form=form)

@users.route("/admin/youth_program", methods=["GET", "POST"])
@login_required
def create_youth_program():
    form = YouthEmpowerMentForm()
    if request.method == "POST":
        file = request.files["subprogram_image"]
        if file:
            image_path = create_path("youth",file)
            program = YouthEmpowerMent(
                    title = form.title.data,
                    content=form.content.data,
                    image_file=image_path,
                    user_id=current_user.id,
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("users.youth_program"))

    return render_template("create_youth.html", form=form)

@users.route("/admin/housing_program", methods=["GET", "POST"])
@login_required
def create_housing_program():
    form = HousingForm()
    if request.method == "POST":
        file = request.files["subprogram_image"]
        if file:
            image_path = create_path("housing",file)
            program = YouthEmpowerMent(
                    title = form.title.data,
                    content=form.content.data,
                    image_file=image_path,
                    user_id=current_user.id,
                    
                    
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("users.housing_program"))

    return render_template("create_housing.html", form=form)

@users.route("/admin/sports_program", methods=["GET", "POST"])
@login_required
def create_sports_program():
    form = SportArtForm()
    if request.method == "POST":
        file = request.files["subprogram_image"]
        if file:
            image_path = create_path("sports",file)
            program = YouthEmpowerMent(
                    title = form.title.data,
                    content=form.content.data,
                    image_file=image_path,
                     user_id=current_user.id,
            )
            db.session.add(program)
            db.session.commit()
            return redirect(url_for("users.sports_program"))

    return render_template("create_sports.html", form=form)



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


@users.route("/admin/blog/<int:blog_id>/delete", methods=["POST"])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog.user != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("users.blog"))


@users.route("/admin/testimonial", methods=["GET", "POST"])
@login_required
def create_testimonial():
    form = TestimonialForm()
    if request.method == "POST":
        file = request.files["profile_image"]
        if file:
            image_path = create_path("testimonial", file)
            testimony = Testimonial(
                name=form.name.data,
                content=form.content.data,
                profile_pic=image_path,
                user_id=current_user.id,
            )
            db.session.add(testimony)
            db.session.commit()
            return redirect(url_for("users.home"))
    return render_template("create_testimonial.html", form=form)


@users.route("/admin/testimonial/<int:testimony_id>/delete", methods=["POST"])
@login_required
def delete_testimony(testimony_id):
    testimony = Testimonial.query.get_or_404(testimony_id)
    if testimony.user != current_user:
        abort(403)
    db.session.delete(testimony)
    db.session.commit()
    return redirect(url_for("users.home"))


@users.route("/admin/gallery", methods=["GET", "POST"])
@login_required
def create_gallery():
    form = GalleryForm()
    if request.method == "POST":
        files = request.files.getlist("files")
        for file in files:
            if file:
                image_file = create_path("gallery", file)
                gallery = Gallery(
                    image_file=image_file,
                    user_id=current_user.id,
                )
                db.session.add(gallery)
                db.session.commit()
        return redirect(url_for("users.gallery"))
    return render_template("create_gallery.html", form=form)


@users.route("/admin/gallery/<int:gallery_id>/delete", methods=["POST"])
@login_required
def delete_gallery(gallery_id):
    gallery = Gallery.query.get_or_404(gallery_id)
    if gallery.user != current_user:
        abort(403)
    db.session.delete(gallery)
    db.session.commit()
    return redirect(url_for("users.gallery"))


@users.route("/admin/logout")
def log_out():
    logout_user()
    return redirect(url_for("users.home"))


# users view


@users.route("/")
def home():
    program = YouthEmpowerMent.query.first()
    testimonials = Testimonial.query.all()
    return render_template("home.html", program=program, testimonials=testimonials)


@users.route("/youths")
def youth_program():

    programs = YouthEmpowerMent.query.all()
    return render_template("youth.html", programs=programs)


@users.route("/communitys")
def community_program():

    programs = Community.query.all()
    return render_template("community.html", programs=programs)


@users.route("/housing")
def housing_program():

    programs = Housing.query.all()
    return render_template("housing.html", programs=programs)


@users.route("/sports")
def sports_program():

    programs = SportsArt.query.all()
    return render_template("sports.html", programs=programs)


# @users.route("/programs/int:program_id/subprograms")
# def sub_program(program_id):
#     program = Program.query.get_or_404(program_id)
#     return render_template('sub_program.html', program=program)


@users.route("/gallery")
def gallery():
    gallerys = Gallery.query.all()

    return render_template("gallery.html", gallerys=gallerys)


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


@users.route("/admin/<int:blog_id>")
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template("blog_detail.html", blog=blog)
