from app import db
from datetime import datetime

class Truck(db.Model):
    id = db.Column('truck_id', db.Integer, primary_key = True)
    truck_station = db.Column(db.String(100))
    parish = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    truck_number = db.Column(db.String(50))
    
    def __init__(self, truck_station, parish, addr, truck_number):
        self.truck_station = truck_station
        self.parish = parish
        self.addr = addr
        self.truck_number = truck_number

class Hydrants(db.Model):
    id = db.Column('hydrant_id',db.Integer, primary_key = True)
    latitude = db.Column(db.Float(10))
    longitude = db.Column(db.Float(10))
    hydrant_type = db.Column(db.String(20))
    
    def __init__(self,latitude,longitude,hydrant_type):
        self.latitude = latitude
        self.longitude = longitude
        self.hydrant_type = hydrant_type
        

class alert(db.Model):
    id = db.Column('incident_id',db.Integer, primary_key = True)
    latitude = db.Column(db.Float(10))
    longitude = db.Column(db.Float(10))
    reported_by = db.Column(db.String(20))
    date_time = db.Column(db.DateTime)
    
    def __init__(self, latitude, longitude, reported_by):
        self.latitude = latitude
        self.longitude = longitude
        self.reported_by = reported_by
    
class Station(db.Model):
    pass

class User(db.Model):
    pass

class IncidentReports(db.Model):
    pass

