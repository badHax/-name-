from app import app
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask_sqlalchemy import SQLAlchemy

import fire_api
#from models import Hydrants, Alert

#@app.before_first_request
#def setup():
    # Recreate database each time for demo
    #db.drop_all()
    #db.create_all()
    
    #debugging
    #db.session.add(Alert(123,321,'dave'))
    #db.session.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    iframe = ""
    return render_template('index.html', iframe=iframe)
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))

@app.route('/mapping')    
def render_map():
    mp = fire_api.Mapping()
    if mp.make_general_map():
        return render_template(app.instance_path()+'mapping.html')

@app.route('/alert', methods=["GET","POST"])
def alert():
    pass

def set_status():
    pass

def add_user():
    pass
