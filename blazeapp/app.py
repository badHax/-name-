from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

import mapping

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://login:pass@localhost/flask_app'

@app.route('/')
def index():
    if(mapping.make_map()):
        return render_template('mapping.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8080))
    app.run(host = '0.0.0.0', port = port)