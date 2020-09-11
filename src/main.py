from flask import Flask
from flask import render_template

from src.controller import home
app = Flask(__name__)
app.register_blueprint(home.bp)
