from flask_sqlalchemy import model
from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class  LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), 
        EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please try a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please try a different email')

class AddSpareForm(FlaskForm):
    brand = StringField('Brand',validators=[DataRequired()])
    model = StringField('Model',validators=[DataRequired()])
    code = IntegerField('Code', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    image = FileField('Image', validator=[FileAllowed('jpg','png','jpeg')])
    submit = SubmitField('Add')