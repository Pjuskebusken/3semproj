from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("home.html", user=current_user)

@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/cancer')
@login_required
def cancer():
    return render_template("cancer.html", user=current_user)

@views.route('/account')
@login_required
def account():
    return render_template("account.html", user=current_user)