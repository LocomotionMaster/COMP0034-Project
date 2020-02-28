from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class SignUpForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(max=50)])
    email = StringField('Email Address',
                        validators=[DataRequired(), Length(max=50), Email()])
    submit = SubmitField('Sign Up')
