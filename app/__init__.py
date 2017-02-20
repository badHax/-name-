from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://login:pass@localhost/flask_app'

app.config['USERNAME'] = 'user'
app.config['PASSWORD'] = 'password'

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

app.config.from_object(__name__)

from app import views