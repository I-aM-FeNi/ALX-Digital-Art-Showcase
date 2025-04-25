from flask import render_template, url_for, flash, redirect
from digitalart import app
from digitalart.forms import RegistrationForm, LoginForm
from digitalart.models import User, Post


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@digitalart.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
