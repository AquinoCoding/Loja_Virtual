from wtforms import Form, BooleanField, StringField, PasswordField, validators


class CadastroForms(Form):

    usuario = StringField('Usuario', [validators.Length(min=4, max=25)])
    nome = StringField('Nome e sobrenome', [validators.Length(min=4, max=32)])
    email = StringField('Email', [validators.Length(min=6, max=25)])

    senha = PasswordField('Nova Senha', [
        validators.DataRequired(), 
        validators.EqualTo('senha_confir')])
        
    senha_confir  = PasswordField('Repita a Senha')

    check_box = BooleanField('Salvar dados?', [validators.DataRequired()])
    
