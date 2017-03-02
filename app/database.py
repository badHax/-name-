from fastkml.kml import KML
import io

#custom imports
from app import db, app
from models import Hydrants, Alert, Station, Truck

class Database(object):
    
    def __init__(self):
        self.setup()

    def add_stations(self):
        try:
            stations = self.kml_to_record(f=app.root_path+'/templates/maps/datasets/stations.kml')
            for station_name in stations:
                station = Station(stations[station_name][0], stations[station_name][1], station_name.translate(None, "\'\"") )
                db.session.add(station)
                db.session.commit()
            db.session.remove()
        except Exception as e:
            print "+++++++++++++++++++++++"
            print e
    
    def add_hydrant(self, lat, lng, type_of):
        try:
            db.session.add(Hydrant(lat,lng,type_of))
        except Exception as e:
            pass

    def add_truck(self, station, parish, addr, num):
        try:
            db.session.add(Truck(station, parish, addr, num))
        except Exception as e:
            pass
        
    def kml_to_record(self,f):
        try:
            record = {}
            locations = self.read_kml(f)
            for name, location in locations.items():
                record.update({name:location})
            return record
        except Exception as e:
            print e
        return ""
    
    def get_stations(self):
        
        stations = Station.query.all()
        
        if stations != None:
            return stations
        return None
        
    def read_kml(self, f):
        kml = KML()
        kml.from_string(open(f).read())
        points = dict()
        for feature in kml.features():
            if feature.styleUrl.startswith('#hf'):
                points.update({feature.name:
                (feature.geometry.y, feature.geometry.x, )})
        return points
    
    def export_geojson(self):
        pass
    
    def import_geojson(self):
        pass
    
    def setup(self):
        self.add_stations()