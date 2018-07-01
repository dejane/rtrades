from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

#The login form
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[InputRequired(),Email(message='Enter a valid email'), Length(max = 60)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)])
    remember = BooleanField('Remember me')

#Account registration  form
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter a valid email'),Length(max=60)])
    username = StringField('Username',validators=[InputRequired(), Length(min=4, max = 20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=30)])
    firstname = StringField('Firstname',validators=[InputRequired(), Length(max = 20)])
    lastname = StringField('Lastname',validators=[InputRequired(), Length(max = 20)])
