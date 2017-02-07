from app import db

class Truck(db.Model):
    __tablename__ = 'Trucks'
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

class Station(db.Model):
    pass


class User(db.Model):
    pass
