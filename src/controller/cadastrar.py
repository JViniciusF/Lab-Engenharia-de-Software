from flask import render_template,Blueprint,request,json
from src.model.doenca import Doenca,Sintomas
from src.model.dadosEpd import DadoEpidemiologico
from src.controller.form import *
from src.database import db_session

bp = Blueprint('cadastrar',__name__,url_prefix='/cadastrar/')


@bp.route('doenca',methods=['GET', 'POST'])
def cadastrarDoenca():
    form = criardoenca()
    if request.method == "POST":
        doenca_nome = request.values["doenca"]
        doenca = Doenca(nome= doenca_nome)
        db_session.add(doenca)
        db_session.commit()
        return render_template("home.html")
    else:
        return render_template("cadastrarDoenca.html",form= form)

@bp.route('sintoma',methods=['GET', 'POST'])
def consulta():
    form = cadastrarSintoma()
    form.doenca.choices = [(doenca.id,doenca.nome) for doenca in Doenca.query.all()]
    if request.method =="POST":
        doenca_id = request.values["doenca"]
        sintoma_Desc = request.values["sintoma"]
        sintoma = Sintomas(descricao=sintoma_Desc, doenca_id = doenca_id)
        db_session.add(sintoma)
        db_session.commit()
        return render_template("home.html")
    else:
        return render_template("cadastrarSintoma.html",form= form)
