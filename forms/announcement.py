from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class CreateAnnouncementForm(FlaskForm):

    title = StringField('Название объекта', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired(), Length(max=300)])
    location = StringField('Адрес', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    advertisement_type = SelectField('Тип объявления', choices=[('flat', 'Квартира'), ('house', 'Дом')],
                                     validators=[DataRequired()])
    square = FloatField('Площадь', validators=[DataRequired()])
    kitchen_square = FloatField('Площадь кухни', validators=[DataRequired()])
    number_of_rooms = IntegerField('Количество комнат', validators=[DataRequired()])
    floor = IntegerField('Этаж', validators=[DataRequired()])
    number_of_floors = IntegerField('Этажи', validators=[DataRequired()])
    year_of_construction = IntegerField('Год постройки', validators=[DataRequired()])
    file = FileField('Фотография', validators=[FileRequired(), FileAllowed(['jpg', 'png'],
                                                                           'Только изображения')])
    is_sell = BooleanField('Продаётся')
    submit = SubmitField('Создать')
