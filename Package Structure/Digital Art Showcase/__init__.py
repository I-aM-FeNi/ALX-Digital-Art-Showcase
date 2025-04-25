from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'  # Replace with a new key if preferred
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digitalart.db'  # Updated database name
db = SQLAlchemy(app)

from digitalartshowcase import routes  # Updated to reflect your project name
