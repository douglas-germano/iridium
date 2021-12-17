from flask import render_template
from flask_login import login_required
from app import app 



@app.route('/')
def main():
    return render_template("main/main.html")

@app.route('/cadastros')
@login_required
def cadastros():
    return render_template("main/cadastros.html")

@app.route('/relatorios')
@login_required
def relatorios():
    return render_template("main/relatorios.html")

@app.route('/manutencoes')
@login_required
def manutencoes():
    return render_template("main/manutencoes.html")