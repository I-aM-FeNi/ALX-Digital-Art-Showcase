from datetime import datetime
from digitalart import db, login_manager  # Added login_manager import
from flask_login import UserMixin  # Added UserMixin import

@login_manager.user_loader  # User loader function for session management
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):  # Inherited from UserMixin for authentication functionality
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(20), unique=True, nullable=False)  # Kept the artist_name field
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # Updated backref to 'author'

    def __repr__(self):
        return f"User('{self.artist_name}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
