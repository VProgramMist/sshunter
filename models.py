from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(255))
    second_name = db.Column(db.String(255))
    gosb = db.Column(db.String(5))
    vsp = db.Column(db.String(5))
    position = db.Column(db.String(50))
