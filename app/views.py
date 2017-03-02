
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import threading

#custom imports
from app import app
from app import db
from app import blaze

mp = blaze.Mapping()

@app.route('/maps/templates/station_view')
def view_stations():
    iframe = mp.show_stations()
    return render_template('maps/templates/station_view.html')
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=["GET","POST"])
def index():
    """
        Main page here
        
    """
    return render_template('index.html')
    
    
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

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def set_status():
    pass

def add_user():
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response