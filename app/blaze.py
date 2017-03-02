import folium       #leaflet mapping library
import pyperclip    #copying and pasting to clipboard
import io           #io
import os, errno
from app import app
import database     #db interface

db = database.Database()
datasets = app.root_path+'/templates/maps/'

"""
# contains methods for generating maps in a web view (iframe)
#
#
# Dependencies
#
# Jinja2
#
# Pandas (Map Data Binding only)
#
# Numpy (Map Data Binding only)
#
# Vincent (Map Data Binding only)
#
#
"""
class Mapping(object):

    #Kingston
    SF_COORDINATES = (18.0179, -76.8099)
    
    #area is a list with two elements - lat and lng
    def make_general_map(self, coordinates=SF_COORDINATES, tiles='StamenToner'):
        mp = folium.Map(location = coordinates, zoom_start=10, tiles=tiles)
        try:
            return mp
        except Exception as ex:
            print ex
            return None
            
            
    def show_stations(self):
        map = self.make_general_map()
        stations = db.get_stations()
        print stations[1].query.get(1).name
        row = 1;
        for station in stations:
            lt, ln, name = station.query.get(row).latitude, station.query.get(row).longitude, station.query.get(row).name
            row = row + 1
            self.make_point_on_map(map, ln, lt, name)
        
        self.silentremove(app.root_path+'/templates/map/templates/station_view.html')
        try:
            map.save(app.root_path+'/templates/maps/templates/station_view.html')
        except Exception as e:
            print e
            return False
            
    
    def map_to_iframe(self, map_file):
        return "<iframe src='app/maps/"+ map_file +".html'></iframe>"
        
    def make_point_on_map(self, map, lat, lng, name):
        map.simple_marker(location=[lat,lng], popup=name, marker_color='red', marker_icon='home')
        #folium.Marker(location=[lat, lng], popup=name).add_to(map)
            
    def make_path_map(self):
        pass
    
    # for shading a general area
    def make_shaped_overlay(self, area, map, name = 'place title'):
        folium.CircleMarker(location=area, radius=50,
                    popup=name, color='#ff0000',
                    fill_color='#ff0000').add_to(map)
    
    def make_path(self):
        pass
    

    def silentremove(self,filename):
        try:
            os.remove(filename)
        except OSError as e: # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                raise # re-raise exception if a different error 

"""
    base class for things that can go on a map
"""
class MapThing(object):
    pass


"""
# contains method for alerting the best possible station
# reroutes if criteria is not met
# criteria may include:
#
#   +   truck may not have water(due to a drought or something) but may still be able to
#       to respond due to a water source (hydrant) being close.
#
#   +   Elevation of of the fire may require trucks  with more suitable pumps
#
#   +   Depending on what is burning there would be an escalation of the fire:
#           -- May require deploying trucks from multiple stations
#           -- irrespective of certain criteria that would otherwise cause the issue to be
#               passed to another station
"""
class Deploy(object):
    #best available
    def dispatch_from_best_station(self):
        pass
    
    def dispatch_next_best(self):
        pass


#  a map as an model
class MapModel(object):
    pass


# a hydrant as an object
class Hydrant(MapThing):
    pass


# a truck as an object
class Truck(MapThing):
    pass


# an alert as an object
#
# based on what is burning there is a code for the weight of the alert
#
class Alert(MapThing):
    pass


# an incident report as an object
class IncidentReport(object):
    pass

"""
class handles data that from reports from previous reports (mainly analytical purposes)

*   make predictive reports
*   custom graphical reports
*   
"""
class Analytics():
    pass
