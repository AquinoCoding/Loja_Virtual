from flask import render_template, session, request, url_for, flash
from loja import app, db
from .forms import CadastroForms

@app.route('/')
def home():
    return 'Seja bem vindo ao sistema em Flask'


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = CadastroForms(request.form)
    if request.method == 'POST' and form.validate():
        flash('Obrigado por fazer seu registro')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title='Cadastro')