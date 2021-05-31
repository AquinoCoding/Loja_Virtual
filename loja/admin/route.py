from flask import render_template, session, request, url_for, flash
from loja import app, db, bcrypt
from .forms import CadastroForms
from .models import SaveMod
import os


@app.route('/')
def home():
    return 'Seja bem vindo ao sistema em Flask'

@app.route('/rules')
def regras():
    return 'Aqui estão as regras do Jogo'


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = CadastroForms(request.form)
    if request.method == 'POST' and form.validate():

        hash_pass = bcrypt.generate_password_hash(forms.senha.data)
        
        user = SaveMod(nome=forms.nome.data, usuario=forms.usuario.data, email=forms.email.data, senha=hash_pass)
        
        
        db_session.add(user)
        flash('Obrigado por fazer seu registro')
        return redirect(url_for('/'))
    return render_template('admin/registrar.html', form=form, title='Cadastro')