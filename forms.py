from flask_wtf import Form
from flask import g
from wtforms import (StringField, PasswordField, validators, FileField,
					TextAreaField, DateField, SelectField)
from wtforms.validators import (DataRequired, Regexp, ValidationError,
								Email, EqualTo)


class Upload(Form):
	image = FileField()
	title = StringField('Start with a clever title...',
						validators=[DataRequired()])
	text = TextAreaField('...change the world...',
						validators=[DataRequired()])


class Login(Form):
	email = StringField('Email',
						validators=[Email(),DataRequired()])
	password = StringField('Password',
							validators=[DataRequired()])
