from flask import render_template,Blueprint 

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/')
def home():
    
    return render_template('hello.html')