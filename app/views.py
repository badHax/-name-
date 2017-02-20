from app import app
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

import mapping

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in')
            return redirect(url_for('add_file'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))
    
def get_alert():
    pass

def set_status():
    pass

def add_user():
    pass
