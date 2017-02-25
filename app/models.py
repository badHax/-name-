from . import db
from datetime import datetime

class Truck(db.Model):
    __tablename__ = 'truck'
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
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Hydrants(db.Model):
    __tablename__ = 'hydrants'
    id = db.Column('hydrant_id',db.Integer, primary_key = True)
    latitude = db.Column(db.Float(10))
    longitude = db.Column(db.Float(10))
    hydrant_type = db.Column(db.String(20))
    
    def __init__(self,latitude,longitude,hydrant_type):
        self.latitude = latitude
        self.longitude = longitude
        self.hydrant_type = hydrant_type
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
        

class Alert(db.Model):
    __tablename__ = 'alert'
    id = db.Column('incident_id',db.Integer, primary_key = True)
    latitude = db.Column(db.Float(10))
    longitude = db.Column(db.Float(10))
    reported_by = db.Column(db.String(20))
    date_time = db.Column(db.DateTime)
    
    def __init__(self, latitude, longitude, reported_by):
        self.latitude = latitude
        self.longitude = longitude
        self.reported_by = reported_by
        self.date_time = datetime.now()
        
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Station(db.Model):
    __tablename__ = 'stations'
    id = db.Column('station_id',db.Integer, primary_key = True)
    latitude = db.Column(db.Float(10))
    longitude = db.Column(db.Float(10))
    name = db.Column(db.String(20))
    
    def __init__(self, latitude, longitude, name):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        
    def __repr__(self):
        return '<id {}>'.format(self.id)

class User(db.Model):
    pass

class IncidentReports(db.Model):
    pass
"""