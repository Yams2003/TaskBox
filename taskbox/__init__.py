from flask import Flask #, render_template, url_for, request, redirect, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db' #telling the run.py where our database is
app.config['SECRET_KEY'] = 'thisisasecretkey'




# Import must be below app variable declaration to avoid a circular import
from taskbox import config, routing