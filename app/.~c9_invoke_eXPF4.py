from app import make_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

from . import views
