import datetime as dt
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class Announcement(SqlAlchemyBase):
    __tablename__ = 'announcements'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    location = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    square = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    visits = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    kitchen_square = sqlalchemy.Column(sqlalchemy.Float, nullable=True) # flat
    number_of_rooms = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    is_sell = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    floor = sqlalchemy.Column(sqlalchemy.Integer, nullable=True) # flat
    number_of_floors = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)#house
    year_of_construction = sqlalchemy.Column(sqlalchemy.Integer, nullable=True) # house
    realtor_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    realtor = orm.relationship("User")
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=dt.datetime.date(dt.datetime.now()))





