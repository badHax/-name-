from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://blazeadmin:blazeapp@localhost/blazeapp'
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'password'
app.config['FIRE_STATIONS_LOCATION'] = 'templates/maps/'
app.secret_key = '012023!!r47j\3yX R~X@H!jmM]Lwf/,?KT'