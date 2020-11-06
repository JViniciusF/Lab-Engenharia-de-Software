from flask import Flask	
from flask import render_template
from src.controller import home,consulta
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(home.bp) 
app.register_blueprint(consulta.bp)
csrf = CSRFProtect(app)

