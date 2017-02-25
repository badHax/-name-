from app import db
from models import Hydrants, Alert, Station

class Database(object):
    
    def setup(self):
        try:
            # Recreate database each time for demo
            db.create_all()
                
            #debugging
            db.session.add(Alert(123,321,'dave'))
            db.session.commit()
            db.session.close()
        except Exception as ex:
            print ex
    
    def get_stations():
        stations = Station.query.all()
        
    def export_geojson(self):
        pass
    
    def import_geojson(self):
        pass