from flask_sqlalchemy import model
from sqlalchemy.sql.functions import count
from . import db, ma
from flask_login import UserMixin
from sqlalchemy.sql import func
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))
    item = db.Column(db.String(50))
    cal = db.Column(db.Float)
    count = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water_count = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    cal_goal = db.Column(db.Float)
    water_goal = db.Column(db.Integer)
    entries = db.relationship("Entry")
    Water_entries = db.relationship("Water")


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class EntrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Entry
        load_instance = True


class WaterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Water
        load_instance = True
