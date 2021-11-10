from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('/views/home.html', user=current_user)


@views.route('/progress')
@login_required
def progress():
    return render_template('/views/progress.html', user=current_user)


@views.route('/profile')
@login_required
def profile():
    return render_template('/views/profile.html', user=current_user)
