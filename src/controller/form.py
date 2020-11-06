from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators,SelectField
from wtforms.validators import DataRequired
from src.model.doenca import Doenca
from src.model.dadosEpd import DadoEpidemiologico

class doencaForm(FlaskForm):
    doenca = SelectField('doenca',choices = [])

# class dadosepdform(FlaskForm):
#     class Meta:
#         model = DadoEpidemiologico
    