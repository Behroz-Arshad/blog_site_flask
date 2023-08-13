from flask import Flask
from flask_blog.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f337b113a9318174a11322ebd6b1fe11'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt=Bcrypt(app)


from flask_blog import routes
