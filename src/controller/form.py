from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators,SelectField
from wtforms.validators import DataRequired
from src.model.doenca import Doenca
from src.model.dadosEpd import DadoEpidemiologico

class doencaForm(FlaskForm):
    doenca = SelectField('Doenca :',choices = [])

class criardoenca(FlaskForm):
    doenca= StringField("Nome da Doenca : ",[validators.required(), validators.length(max=30)])
    
class cadastrarSintoma(FlaskForm):
    doenca = SelectField('Doenca :',choices = [])
    sintoma= StringField("Sintoma : ",[validators.required(), validators.length(max=50)])