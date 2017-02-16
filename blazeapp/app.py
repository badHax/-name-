from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
import os

#script that generates the map views
import mapping

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://login:pass@localhost/flask_app'

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/')
def index():
    #should be login
    return render_template('home.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8080))
    app.run(host = '0.0.0.0', port = port)