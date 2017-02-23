from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object('config')
#db.create_all()
#db.session.commit()
from . import views