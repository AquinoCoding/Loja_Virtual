from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators

class AdicionarProdutos(Form):

    nome = StringField('Nome: ',[validators.DataRequired()])
    valor = IntegerField('Preço: ', [validators.DataRequired()])
    desconto = IntegerField('Desconto: ', [validators.DataRequired()])
    quantidade = IntegerField('Quantidade: ', [validators.DataRequired()])

    descricao = TextAreaField('Descrição: ', [validators.DataRequired()])
    cores = TextAreaField('Cores: ', [validators.DataRequired()])

    image_1 = FileField('Imagem 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Imagem 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Imagem 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

