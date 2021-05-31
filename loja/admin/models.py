from enum import Flag, unique

from sqlalchemy.orm import defaultload
from loja import db

class SaveMod(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(40), unique=True, nullable=False)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')


    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
