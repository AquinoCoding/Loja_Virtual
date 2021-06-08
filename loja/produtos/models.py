from flask.scaffold import F
from sqlalchemy.orm import backref, defaultload
from loja import db
from datetime import datetime

class AddProdutos(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(15), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    desconto = db.Column(db.Integer, default=0)
    quantidade = db.Column(db.Integer, nullable=False)

    descricao = db.Column(db.Text, nullable=False)
    cores = db.Column(db.Text, nullable=False)
    
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.id'), nullable=False)
    marca = db.relationship('Marcas', backref=db.backref('marca', lazy=True))

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    categoria = db.relationship('Categorias', backref=db.backref('categorias', lazy=True))

    img_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    img_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    img_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

    def __repr__(self):
        return '<AddProdutos %r>' % self.nome

class Marcas(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False, unique=True)

class Categorias(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False, unique=True)

db.create_all()