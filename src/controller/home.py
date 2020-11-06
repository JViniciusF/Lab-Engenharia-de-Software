from flask import render_template,Blueprint 
from src.controller.form import doencaForm
from src.model.doenca import Doenca

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('')
def home():
    form = doencaForm()
    form.doenca.choices = [(doenca.nome) for doenca in Doenca.query.all()]
    
    return render_template('home.html',form = form)
