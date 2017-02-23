from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:passtheword@localhost/blazeapp'
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'password'
app.secret_key = '012023!!r47j\3yX R~X@H!jmM]Lwf/,?KT'
