from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm, RegistrationForm  # We will define these in forms.py

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Required for secure forms

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
def index():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Use the login form
    if form.validate_on_submit():
        if form.email.data == 'test@example.com' and form.password.data == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)

# Registration route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # Use the registration form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__ == "__main__":
    app.run(debug=True)
