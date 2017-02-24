from app import db
from models import Hydrants, Alert

class Database(object):
    
    def setup(self):
        # Recreate database each time for demo
        db.drop_all()
        db.create_all()
            
        #debugging
        db.session.add(Alert(123,321,'dave'))
        db.session.commit()
    
    
    def export_geojson(self):
        pass
    
    def import_geojson(self):
        pass