from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    body = CKEditorField("Body", validators=[DataRequired()])
    submit = SubmitField("Add post")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")