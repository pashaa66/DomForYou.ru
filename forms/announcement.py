from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField,FileField
from wtforms.validators import DataRequired


class CreateAnnouncementForm(FlaskForm):
    advertisement_type = SelectField('Тип объявления', choices=[('flat', 'Квартира'), ('house', 'Дом')], validators=[DataRequired()])
    title = StringField('Название объекта', validators=[DataRequired()])
    price = IntegerField('Цена',validators=[DataRequired()])
    square = FloatField('Площадь', validators=[DataRequired()])
    files = FileField('Фотографии', validators=[DataRequired()])
    # flat
    # floor = IntegerField('Этаж', validators=[DataRequired()])
    number_of_rooms = IntegerField('Количество комнат', validators=[DataRequired()])
    # house
    submit = SubmitField('Создать')
