from flask_login import LoginManager, login_user
from wtforms import Form, StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask import Flask, config
import sys

class LoginForm(FlaskForm):
    username = StringField('UserName')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')

class Config(object):
    SECRET_KEY = 'my-secrete-key'   


__all__ = [
    "main",
    "auth",
    "LoginForm",
    "LoginManager",
    "Config",
    "Bootstrap",
    "Flask",
    "config",
    "login_user",
    "sys"
]



