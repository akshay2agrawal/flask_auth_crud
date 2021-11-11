from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from .main import main 
from . import LoginForm, login_user
from flask_login import login_required, current_user, logout_user

auth = Blueprint('auth', __name__)


@auth.route("/login", methods = ['POST', 'GET'])
#@login_required
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.username.data).first()
            if not user or not check_password_hash(user.password, form.password.data):
                flash('Please check your login details and try again.')
                return redirect(url_for('auth.login'))
            login_user(user, remember=True) #remember is for remember me like if just in case the user closes the browser. The session will still be there.
            return redirect(url_for('main.profile'))
    return render_template('login.html', form = form)

@auth.route("/signup", methods = ['POST','GET'])
def signup():

    if request.method == "POST":

        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash("Email address already exists")
            redirect(url_for(auth.signup))

        new_user = User(name=name, email=email, password=generate_password_hash(password, method="sha256"))
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template('signup.html')


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))
