from flask import render_template, session, request, url_for, flash, redirect
from loja import app, db, bcrypt
from .forms import CadastroForms
from .models import SaveMod
import os


@app.route('/')
def home():
    return 'Seja bem vindo ao sistema em Flask'

@app.route('/tela')
def regras():
    return 'Cadastro Feito com sucesso'


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = CadastroForms(request.form)
    if request.method == 'POST' and form.validate():

        hash_pass = bcrypt.generate_password_hash(form.senha.data)
        user = SaveMod(usuario=form.usuario.data, nome=form.nome.data,  email=form.email.data, senha=hash_pass)
        
        db.session.add(user)
        flash('Obrigado por fazer seu registro')
        return redirect(url_for('tela'))

    return render_template('admin/registrar.html', form=form, title='Cadastro')