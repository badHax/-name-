from app import app
from app import db
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask_sqlalchemy import SQLAlchemy

#custom imports
from app import fire_api
from app import database

mp = fire_api.Mapping()

@app.before_first_request
def setup():
   db = database.Database()
   db.setup()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=["GET","POST"])
def index():
    """
        Main page here
        
    """
    mp.make_general_map('index_map')
    return render_template('index.html')

@app.route('/m')
def m():
    return render_template('/maps/index_map.html')
    
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

@app.route('/alert', methods=["GET","POST"])
def alert():
    pass

def set_status():
    pass

def add_user():
    pass
