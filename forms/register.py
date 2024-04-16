from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, StringField, IntegerField, TelField
from wtforms.validators import DataRequired


class RegisterFormUser(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegisterFormRealtor(FlaskForm):
    name = StringField('Имя риэлтора', validators=[DataRequired()])
    surname = StringField('Фамилия риэлтора', validators=[DataRequired()])
    age = IntegerField('Возраст риэлтора', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    phone_number = TelField('Номер телефона', validators=[DataRequired()])
    experience = IntegerField('Стаж работы', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')