from flask import render_template,Blueprint 
from src.model.doenca import Doenca,Sintomas
from src.model.dadosEpd import DadoEpidemiologico
from src.controller.form import doencaForm

bp = Blueprint('consulta', __name__, url_prefix='/consulta/')

@bp.route('sintomas')
def consulta():
    form = doencaForm()
    form.doenca.choices = [(doenca.nome) for doenca in Doenca.query.all()]
    return render_template("consultaSintomas.html",form= form)
