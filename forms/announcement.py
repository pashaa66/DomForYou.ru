from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, F
from wtforms.validators import DataRequired


class CreateAnnouncement(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    square = FloatField('Площадь', validators=[DataRequired()])
    number_of_rooms = IntegerField('Количество комнат', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
