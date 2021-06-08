from datetime import time
from flask import redirect, render_template, url_for, flash, request
from loja import db, app, photos
from .forms import AdicionarProdutos
from .models import Marcas, Categorias


@app.route('/cadastro-marcas', methods=['GET', 'POST'])
def cadastro_marca():

    if request.method == 'POST':
        getmarca = request.form.get('marca')
        marca = Marcas(nome=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('cadastro_marca'))

    return render_template('/produtos/addmarca.html',
                           marcas='marcas',
                           title='Cadastro de Marcas')


@app.route('/cadastro-categorias', methods=['GET', 'POST'])
def cadastro_categ():

    if request.method == 'POST':
        getcat = request.form.get('categoria')
        categoria = Categorias(nome=getcat)
        db.session.add(categoria)
        flash(f'A Categoria {getcat} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('cadastro_categ'))

    return render_template('/produtos/addmarca.html',
                           title='Cadastro de Categorias')


@app.route('/cadastro-produtos', methods=['GET', 'POST'])
def adicionar_prod():
    marcas = Marcas.query.all()
    categorias = Categorias.query.all()
    form = AdicionarProdutos(request.form)
    if request.method == 'POST':
        photos.save(request.files.get('img_1'))
        photos.save(request.files.get('img_2'))
        photos.save(request.files.get('img_3'))
        #flash('Produto Cadastrado com Sucesso', 'success')
    return render_template('produtos/adicionarprodutos.html',
                           title='Cadastrar Produto',
                           form=form,
                           marcas=marcas,
                           categorias=categorias)
