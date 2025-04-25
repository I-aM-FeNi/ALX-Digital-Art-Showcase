from datetime import datetime
from digitalartshowcase import db, login_manager  # Ensure this matches your project structure
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(20), unique=True, nullable=False)  # Renamed 'username' to 'artist_name'
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='artist', lazy=True)  # Renamed 'author' to 'artist'

    def __repr__(self):
        return f"User('{self.artist_name}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artwork_title = db.Column(db.String(100), nullable=False)  # Renamed 'title' to 'artwork_title'
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Renamed 'user_id' to 'artist_id'

    def __repr__(self):
        return f"Post('{self.artwork_title}', '{self.date_posted}')"
