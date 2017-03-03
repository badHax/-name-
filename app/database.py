from fastkml.kml import KML
import threading
import io

#custom imports
from app import db, app
from models import Hydrant, Alert, Station, Truck

class Database(object):
    def __init__(self):
        self.setup()
        
    def add_stations(self):
        try:
            stations = self.kml_to_record(app.root_path+'/templates/maps/datasets/stations.kml')
            for station_name in stations:
                station = Station(stations[station_name][0], stations[station_name][1], station_name.translate(None, "\'\"") )
                db.session.add(station)
                db.session.commit()
            db.session.remove()
        except Exception as e:
            db.session.rollback()
            print e
    
    def add_hydrants(self):
        hydrants = self.kml_to_record(app.root_path+'/templates/maps/datasets/hydrants.kml')
        for item in hydrants:
            lt, ln, name = hydrants[item][0], hydrants[item][1],item.translate(None,"\'\"")
            try:
                if db.session.query(Hydrant).filter_by(hydrant_type=name).first():
                    continue
                else:
                    hydrant= Hydrant(ln,lt,name)
                    db.session.add(hydrant)
                    db.session.commit()
            except Exception as e:
                db.session.rollback()
                print e[0]
                
    def add_trucks(self):
        try:
            pass
        except Exception as e:
            pass
        
    def kml_to_record(self,f):
        record = {}
        locations = self.read_kml(f)
        for name, location in locations.items():
            try:
                record.update({name:location})
            except Exception as e:
                 print e
        return record
    
    def get_stations(self):
        stations = Station.query.all()
        if stations != None:
            return stations
        return None
    
    def get_hydrants(self):
        hydrants = Hydrant.query.all()
        if hydrants != None:
            return hydrants
        return None
        
    def read_kml(self, f):
        kml = KML()
        kml.from_string(open(f).read())
        points = dict()
        for feature in kml.features():
            points.update({feature.name:
            (feature.geometry.y, feature.geometry.x, )})
        return points
    
    def export_geojson(self):
        pass
    
    def import_geojson(self):
        pass
    
    def setup(self):
        self.add_hydrants()
        #self.add_stations()
        