from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateAnnouncementForm(FlaskForm):
    advertisement_type = SelectField('Тип объявления', choices=[('flat', 'Квартира'), ('plot', 'Участок')], validators=[DataRequired()])
    title = StringField('Название объекта', validators=[DataRequired()])
    price = IntegerField('Цена',validators=[DataRequired()])
    number_of_rooms = IntegerField('Количество комнат', validators=[DataRequired()])
    square = IntegerField('Площадь', validators=[DataRequired()])
    submit = SubmitField('Submit')
