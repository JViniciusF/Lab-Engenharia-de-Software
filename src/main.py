from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/nome/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
@app.route('/onde')
def onde(lista = None):
    lista1 =['familia','amigos','paixão']
    return render_template('Outro.html',lista = lista1)