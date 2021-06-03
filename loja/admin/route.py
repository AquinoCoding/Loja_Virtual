from operator import index
import re
from flask import render_template, session, request, url_for, flash, redirect
from wtforms.validators import Email
from loja import app, db, bcrypt
from .forms import CadastroForms, LoginForms
from .models import UserMod
import os

# Definidor de nome da rota visual no navegador
@app.route('/admin')

# Definidor do nome da rota no código conforme o nome da função
def admin():
    if 'email' not in session:
        flash('Nada foi encontrado, se cadastre ou faça login novamente', 'danger')
        return redirect(url_for('login'))

    return render_template('admin/index.html', title='Gerenciador de Página')



@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = CadastroForms(request.form)

# Validação de dados conforme o banco de dados e implementação da

    if request.method == 'POST' and form.validate():

# encryptografia na senha

        hash_pass = bcrypt.generate_password_hash(form.senha.data)
        user = UserMod(usuario=form.usuario.data, nome=form.nome.data,  email=form.email.data, senha=hash_pass)

# Salvamento no banco de dados

        db.session.add(user)
        db.session.commit()

# Mensagens e redirecinamento do para a página pós cadastro

        flash(f'{form.nome.data} Obrigado por fazer seu registro', 'sucess')
        return redirect(url_for('admin'))

# Renderização do template da página

    return render_template('admin/registrar.html', form=form, title='Cadastro')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForms(request.form)
    

    if request.method == 'POST' and form.validate():

        user = UserMod.query.filter_by(email=form.email.data).first() 

        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            session['email'] = form.email.data
            flash(f'{form.email.data} Login feito com sucesso', 'sucess')
            return redirect(request.args.get('next') or url_for('admin'))
        else: 
            flash('Email ou Senha Incorreto', 'danger')

    return render_template('admin/login.html', form=form, title='Login')
 