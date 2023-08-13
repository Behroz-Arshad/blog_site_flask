from flask_blog.models import User, Post
from flask_blog.forms import RegistrationForm, LoginForm
from flask import render_template, flash, redirect, url_for
from flask_blog import app, db, bcrypt
posts = [
    {
        "author": "M Behroz",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20, 2020"
    },
    {
        "author": "Usman",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 10, 2020"
    },
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Sign up', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)

#
# @app.route('/account')
#     @login_required
# def account():
#     image_file = url_for('static', filename='image/'+current_user.image_file)
#     return render_template('account.html')