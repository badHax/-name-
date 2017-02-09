import app
from app import db
from flask.ext.restless import APIManager

manager = APIManager(app, flask_sqlalchemy_db=db)


#needs work