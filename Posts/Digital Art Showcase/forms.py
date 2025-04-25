from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from digitalartshowcase.models import User  # Make sure this matches your project structure

class RegistrationForm(FlaskForm):
    # Renaming 'Username' to 'Artist Name' to align with the theme of the app
    artist_name = StringField('Artist Name',
                              validators=[DataRequired(), Length(min=2, max=20)])  # Artist name length validation
    
    email = StringField('Email Address',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Create Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])

    # Custom submit button to reflect the artistic theme
    submit = SubmitField('Join the Art Collective')

    # Validation for artist name uniqueness
    def validate_artist_name(self, artist_name):
        user = User.query.filter_by(artist_name=artist_name.data).first()
        if user:
            raise ValidationError('That artist name is taken. Please choose a different one.')

    # Validation for email uniqueness
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email Address',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Enter Password', validators=[DataRequired()])
    
    remember = BooleanField('Stay Signed In')
    
    # Personalized submit button
    submit = SubmitField('Enter Your Art Space')


class UpdateAccountForm(FlaskForm):
    artist_name = StringField('Artist Name',
                              validators=[DataRequired(), Length(min=2, max=20)])  # Validation for artist name
    
    email = StringField('Email Address',
                        validators=[DataRequired(), Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])  # File upload for profile picture
    submit = SubmitField('Update Your Profile')

    # Artist name uniqueness validation during updates
    def validate_artist_name(self, artist_name):
        if artist_name.data != current_user.artist_name:
            user = User.query.filter_by(artist_name=artist_name.data).first()
            if user:
                raise ValidationError('That artist name is taken. Please choose a different one.')

    # Email uniqueness validation during updates
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


# Adding a form for post submissions (optional based on your vision)
class PostForm(FlaskForm):
    title = StringField('Title of Artwork', validators=[DataRequired()])
    content = TextAreaField('Artwork Description', validators=[DataRequired()])  # Using TextAreaField for longer content
    submit = SubmitField('Post Artwork')  # Button name reflecting the submission of artwork
