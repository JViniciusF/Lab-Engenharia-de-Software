from flask import render_template,Blueprint,request,json
from src.model.doenca import Doenca,Sintomas
from src.model.dadosEpd import DadoEpidemiologico
from src.controller.form import doencaForm

bp = Blueprint('consulta',__name__,url_prefix='/consulta/')

@bp.route('sintomas')
def consulta():
    form = doencaForm()
    form.doenca.choices = [(doenca.id,doenca.nome) for doenca in Doenca.query.all()]
    return render_template("consultaSintomas.html",form= form)

@bp.route('ajaxSintomas',methods=['GET', 'POST'])
def voltaSintomas():
    doenca_id = request.args["doenca"]
    sintomas = Sintomas.query.filter_by(doenca_id = doenca_id)

    aux = []
    for sintoma in sintomas:
        aux.append(sintoma.descricao)
        print(aux)
    return json.dumps(aux)