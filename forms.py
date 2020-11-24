from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField,\
    TextAreaField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError, Email
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={'placeholder': 'your username'})
    password = PasswordField('password', validators=[DataRequired(), Length(8, 128)], \
                             render_kw={'placeholder': 'your password'})
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log in")




