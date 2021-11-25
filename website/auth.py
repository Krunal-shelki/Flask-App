from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    flash,
    redirect,
    url_for,
)

# from sqlalchemy.sql.expression import true
# from sqlalchemy.sql.functions import user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from website import auth

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, Try again!", category="error")
        else:
            flash("User does not exist!", category="error")
    return render_template("/auth/login.html", user=current_user)


@auth.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        gender = request.form.get("gender")
        age = request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
        calGoal = request.form.get("calGoal")
        waterGoal = request.form.get("waterGoal")
        password = request.form.get("password")
        passcnf = request.form.get("passcnf")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("User already Exists!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 charecters", category="error")
        elif len(name) < 2:
            flash("name must be greater than 1 charecters", category="error")
        elif password != passcnf:
            flash("password does not match to confirm password", category="error")
        elif len(password) < 7:
            flash("password must be greater than 6 charecters", category="error")
        else:
            new_user = User(
                email=email,
                password=generate_password_hash(password, method="sha256"),
                name=name,
                gender=gender,
                age=age,
                height=height,
                weight=weight,
                water_goal=waterGoal,
                cal_goal=calGoal,
            )
            db.session.add(new_user)
            db.session.commit()
            flash("acc created", category="success")
            return redirect(url_for("views.home"))

    return render_template("/auth/signin.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
