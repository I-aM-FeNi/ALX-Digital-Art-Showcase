from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    # Renaming 'Username' to 'Artist Name' to keep the theme consistent
    artist_name = StringField('Artist Name',
                              validators=[DataRequired(), Length(min=2, max=20)])  # Artist name length validation
    
    email = StringField('Email Address',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Create Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    # Button with a personalized creative touch
    submit = SubmitField('Join the Art Collective')


class LoginForm(FlaskForm):
    email = StringField('Email Address',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Enter Password', validators=[DataRequired()])
    
    remember = BooleanField('Stay Signed In')
    
    # A personalized login button for artists
    submit = SubmitField('Enter Your Art Space')
