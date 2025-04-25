from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'  # Replace with a new key if preferred
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digitalart.db'  # Updated database name

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Configure login manager
login_manager.login_view = 'login'  # Name of the login view function
login_manager.login_message_category = 'info'  # Flash message category for login messages

from digitalartshowcase import routes  # Updated to reflect your project name