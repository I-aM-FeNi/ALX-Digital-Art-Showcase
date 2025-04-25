from flask import render_template, url_for, flash, redirect, request
from digitalart import app, db, bcrypt
from digitalart.forms import RegistrationForm, LoginForm
from digitalart.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Dummy data for artist posts
posts = [
    {
        'artist_name': 'Luna Vortex',
        'title': 'Abstract Dreams',
        'content': 'Exploring the vivid landscapes of the subconscious mind.',
        'date_posted': 'September 24, 2024'
    },
    {
        'artist_name': 'Orion Starlight',
        'title': 'Cosmic Wonders',
        'content': 'A deep dive into the mysteries of space through digital art.',
        'date_posted': 'September 22, 2024'
    },
    {
        'artist_name': 'Aether Mirage',
        'title': 'Illusions of Light',
        'content': 'Playing with light and shadows to craft surreal environments.',
        'date_posted': 'September 20, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  # Redirect logged-in users from registering
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hashing the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Create new user
        user = User(artist_name=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))  # Redirect to login page after registration
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Redirect logged-in users from logging in again
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Querying user by email
        user = User.query.filter_by(email=form.email.data).first()
        # Checking if user exists and if the password matches
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Logging in the user
            login_user(user, remember=form.remember.data)
            # Redirecting to the next page if specified, otherwise home
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()  # Logging the user out
    return redirect(url_for('home'))

@app.route("/account")
@login_required  # Ensure only logged-in users can access the account page
def account():
    return render_template('account.html', title='Account')
